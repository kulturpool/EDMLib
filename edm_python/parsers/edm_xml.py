from rdflib import Graph, URIRef, Literal, RDF


from ..edm import (
    EDM_Record,
    EDM_Namespace,
    Literal,
    EDM_ProvidedCHO,
    EDM_WebResource,
    ORE_Aggregation,
    URIRef,
    CC_License,
    SKOS_Concept,
    EDM_Agent,
    EDM_Place,
    EDM_TimeSpan,
    SVCS_Service,
    LiteralType,
    URIRefType,
)

from typing import get_type_hints, List, Any, Dict

from pydantic import ValidationError


def check_if_many(cls: object, attname: str) -> bool:
    """
    Checks against an objects type annotation if the attribute with 'attname' expects a list of values or a single value. I.e. checks the
    cardinality of a property in the context of a spefic class.
    """
    hints = get_type_hints(cls).get(attname)
    if hints and (
        str(hints).startswith("typing.Optional[typing.List")
        or str(hints).startswith("typing.List")
        or str(hints).startswith("typing.Union[typing.List")
    ):
        return True
    else:
        return False


def to_literal(literal: Literal):
    """
    Temporary helper function to convert rdflib.Literal to edm_python.edm.LiteralType
    """
    return LiteralType(
        lexical_or_value=literal.value, lang=literal.language, datatype=literal.datatype
    )


def to_ref(ref: URIRef):
    """
    Temporary helper function to convert rdflib.URIRef to edm_python.edm.URIRefType
    """
    print("----> creating ref for", type(ref), ref)
    print("----> creating ref for", type(ref), ref)

    # prefix, namespace, identifier = graph.compute_qname(ref)
    value = str(ref)
    res = URIRefType(value=value)
    print(res, ref, str(ref))
    return res


def cls_attribute_to_ref(attname: str) -> URIRef:
    """
    Helper that converts a edm_classes attribute name to the corresponding properties full IRI.
    """
    res = attname.split("_")
    if attname.startswith("WGS84_POS"):
        ns = "WGS84_POS"
    else:
        ns = res[0]

    if len(res) > 2:
        res = "_".join(res[1:])
    else:
        res = res[1]

    return URIRef(f"{getattr(EDM_Namespace, ns.upper())}{res}")


def cls_attribute_to_ref_new(attname: str) -> URIRef:
    """
    Helper that converts a edm_classes attribute name to the corresponding properties full IRI.
    """
    res = attname.split("_")
    if attname.startswith("wgs84_pos"):
        ns = "WGS84_POS"
        res = attname.replace("wgs84_pos_", "")
    else:
        ns = res[0]

        if len(res) > 2:
            res = "_".join(res[1:])
        else:
            res = res[1]

    return URIRef(f"{getattr(EDM_Namespace, ns.upper())}{res}")


def get_attributes(cls: object) -> Dict[str, URIRef]:
    """
    For a given edm-class, get a list of all its properties as edm_python.edm.Ref objects.
    """
    attlist = list(cls.__dict__.get("__annotations__").keys())  # type: ignore
    return {el: cls_attribute_to_ref_new(el) for el in attlist}


def convert(lit_or_ref: URIRef | Literal):
    """
    Helper to convert a rdlib.URIRef or rdflib.Literal to the
    corresponding edm-python object.
    """
    print("lit_or_ref is", type(lit_or_ref), lit_or_ref)
    if isinstance(lit_or_ref, URIRef):
        print("called to ref")
        return to_ref(lit_or_ref)
    elif isinstance(lit_or_ref, Literal):  # type: ignore
        print("called to literal")
        return to_literal(lit_or_ref)


class EDM_Parser:
    """
    Parser for edm-xml records. Returns an edm_python.edm.EDM_Record object.
    """

    def __init__(self, graph: Graph):
        self.graph: Graph = graph

    def get_single_ref(self, obj_cls: object) -> URIRef:
        """
        Loooks up instances of a given obj_cls (a edm_python edm-class) and returns
        a single IRI.
        This method expects that the cardinality of the obj_cls is one per record.
        """
        res = self.get_many_ref(obj_cls)
        assert len(res) == 1
        print("in get single ref: ", res[0])
        return res[0]

    def get_many_ref(self, obj_cls: object) -> List[URIRef]:
        """
        Loooks up instances of a given obj_cls (a edm_python edm-class) and returns
        a list of instance-IRIs.
        This method expects that the cardinality of the obj_cls is one or more.
        """
        # TODO: check assertion that subjects are always uri-refs...
        return [
            el[0]  # type: ignore
            for el in self.graph.triples((None, RDF.type, obj_cls.get_class_ref()))  # type: ignore
        ]

    def get_triples(self, ref: URIRef):
        """
        Return all predicate-object triples for a given URIRef within the instance`s-graph.
        """
        return self.graph.predicate_objects(ref)

    def get_aggregation(self):
        agg = list(
            self.graph.triples((None, RDF.type, ORE_Aggregation.get_class_ref()))
        )
        assert len(agg) == 1
        return agg[0][0]

    def get_webresources(self):
        webresources = list(
            self.graph.triples((None, RDF.type, EDM_WebResource.get_class_ref()))
        )
        print("WEB-REsources", webresources)
        res = [el[0] for el in webresources]
        print(res)
        return res

    def get_instance_triples(self, instance: URIRef, cls_obj: object) -> Dict[str, Any]:
        attribs = get_attributes(cls_obj)
        temp: Dict[str, Any] = {}
        for att, ref in attribs.items():
            values = [
                convert(el[2])  # type: ignore
                for el in list(self.graph.triples((instance, ref, None)))
            ]
            if values:
                many = check_if_many(cls_obj, att)
                if not many:
                    assert (
                        len(values) == 1
                    ), f"Expected 1 value but got {len(values)}; {cls_obj=}; {att=}"
                    values = values[0]
                temp.update({att: values})
        print("instance_triples", temp)
        return temp

    def parse_single_class(self, cls_obj: object) -> Any:
        add = {}
        match cls_obj.__name__:  # type: ignore
            case "EDM_ProvidedCHO":
                inst = self.get_single_ref(cls_obj)
            case "ORE_Aggregation":
                inst = self.get_aggregation()
                add = {
                    "edm_provider": LiteralType(
                        lexical_or_value="Kulturpool", lang="de"
                    ),
                    "edm_rights": URIRefType(
                        value="http://example.com/placeholder_rights"
                    ),
                }
            case _:  # type: ignore
                pass
        triples = self.get_instance_triples(inst, cls_obj)  # type: ignore

        triples.update(**add)
        return cls_obj(id=URIRefType(value=str(inst)), **triples)  # type: ignore

    def parse_many_class(self, cls_obj: Any) -> List[Any]:
        match cls_obj.__name__:
            case "EDM_WebResource":
                instances = self.get_webresources()
            case _:
                instances = self.get_many_ref(cls_obj)
        res: List[Any] = []
        for inst in instances:
            print("instance", type(inst), inst)
            res.append(
                cls_obj(
                    id=URIRefType(value=str(inst)),
                    **self.get_instance_triples(inst, cls_obj),
                )  # type: ignore
            )

        return res

    def parse(self):
        cho = self.parse_single_class(EDM_ProvidedCHO)
        aggre = self.parse_single_class(ORE_Aggregation)
        web_resources = self.parse_many_class(EDM_WebResource)
        skos_concepts = self.parse_many_class(SKOS_Concept)
        edm_time_spans = self.parse_many_class(EDM_TimeSpan)
        edm_agents = self.parse_many_class(EDM_Agent)
        edm_places = self.parse_many_class(EDM_Place)
        cc_licenses = self.parse_many_class(CC_License)
        svcs_services = self.parse_many_class(SVCS_Service)

        return EDM_Record(
            provided_cho=cho,
            aggregation=aggre,
            web_resource=web_resources,
            skos_concept=skos_concepts,
            edm_time_span=edm_time_spans,
            edm_agent=edm_agents,
            edm_place=edm_places,
            cc_license=cc_licenses,
            svcs_service=svcs_services,
        )
