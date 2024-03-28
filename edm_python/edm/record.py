from typing import List

from pydantic import BaseModel
from rdflib import Graph

from .classes import (
    CC_License,
    EDM_Agent,
    EDM_Place,
    EDM_ProvidedCHO,
    EDM_TimeSpan,
    EDM_WebResource,
    ORE_Aggregation,
    SKOS_Concept,
    SVCS_Service,
)
from .enums import EDM_Namespace

__all__ = ["EDM_Record"]


class EDM_Record(BaseModel):
    """
    Pydantic model representing an edm record, as a fully typed structure.

    Validation:
    This model is responsible for validating the overall structure, order and completeness
    of the record.
    The individual models for each of its properties are responsible for validating their own attributes –
    the completeness, cardinality and order of their members.
    Finally, the value dataclasses (Ref, RDF_Literal) within those container types are responsible for validating
    the indiviudal values.
    """

    # model_config = ConfigDict(strict=False)
    provided_cho: EDM_ProvidedCHO
    aggregation: ORE_Aggregation
    web_resource: List[EDM_WebResource] | None = None
    skos_concept: List[SKOS_Concept] | None = None
    edm_agent: List[EDM_Agent] | None = None
    edm_time_span: List[EDM_TimeSpan] | None = None
    edm_place: List[EDM_Place] | None = None
    cc_license: List[CC_License] | None = None
    svcs_service: List[SVCS_Service] | None = None

    def get_rdf_graph(self):
        """
        Return whole record as as an RDF - rdflib.Graph object.
        """
        graph = Graph()
        namespaces = EDM_Namespace.get_namespace_tuples()
        for tup in namespaces:
            graph.bind(tup[0].lower(), tup[1])
        # TODO: abstract the instance list into a callable hook
        for instance in [
            "provided_cho",
            "web_resource",
            "aggregation",
            "skos_concept",
            "edm_agent",
            "edm_time_span",
            "edm_place",
            "cc_license",
            "svcs_service",
        ]:
            attval = getattr(self, instance)
            if attval:
                if isinstance(attval, list):
                    for val in attval:  # type: ignore
                        # print("val was list for", val, attval) # type: ignore
                        triples = val.get_triples()  # type: ignore
                        [graph.add(triple) for triple in triples]  # type: ignore
                else:
                    # print("val was not a list for", attval)
                    triples = attval.get_triples()
                    [graph.add(triple) for triple in triples]
        return graph

    def serialize(self, format: str = "pretty-xml", max_depth: int = 1):
        """
        Serialize graph to rdf/xml with pretty-formatting.
        TODO: the returned xml is not yet edm conform, i.e. the ordering of the xml elements is not enforced.
        TODO: enforce the order of elements with a simple xslt transformation
        """
        graph = self.get_rdf_graph()

        return graph.serialize(format=format, max_depth=max_depth)
