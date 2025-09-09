from pydantic import ValidationError
from edmlib import EDM_Parser, EDM_Record, EDM_ProvidedCHO, ORE_Aggregation, Ref, Lit
from rdflib import Graph, URIRef


def test_parse_xml(file_edm_record_minimal):
    validation_errors = []

    try:
        EDM_Parser.from_string(file_edm_record_minimal.decode("utf-8")).parse()
    except ValidationError as e:
        validation_errors.extend([error.get("msg") for error in e.errors()])

    assert (
        "Assertion failed, URIs of providedCHO and aggregation.edm_aggregatedCHO do not match: self.provided_cho.id.value='https://uri.test/edm123%C3%BC' != self.aggregation.edm_aggregatedCHO.value='https://uri.test/edm123ü'."
        not in validation_errors
    )


def test_construct_programmatically():
    validation_errors = []

    try:
        EDM_Record(
            provided_cho=EDM_ProvidedCHO(
                id=Ref(value="https://uri.test/edm123ü"),
                dc_type=[Lit(value="Text", lang="en")],
                dc_title=[Lit(value="Titel", lang="de")],
                dc_identifier=[Lit(value="123")],
                dc_language=[Lit(value="de")],
                edm_type=Lit(value="TEXT"),
            ),
            aggregation=ORE_Aggregation(
                id=Ref(value="http://uri.test/edm123#Aggregation"),
                edm_aggregatedCHO=Ref(value="https://uri.test/edm123ü"),
                edm_dataProvider=Lit(value="Test"),
                edm_isShownAt=Ref(value="http://uri.test/edm123.jpg"),
                edm_isShownBy=Ref(value="http://uri.test/edm123.jpg"),
                edm_provider=Lit(value="Kulturpool"),
                edm_rights=Ref(
                    value="http://creativecommons.org/licenses/by-nc-sa/4.0/"
                ),
            ),
        )
    except ValidationError as e:
        validation_errors.extend([error.get("msg") for error in e.errors()])

    assert (
        "Assertion failed, URIs of providedCHO and aggregation.edm_aggregatedCHO do not match: self.provided_cho.id.value='https://uri.test/edm123%C3%BC' != self.aggregation.edm_aggregatedCHO.value='https://uri.test/edm123ü'."
        not in validation_errors
    )


def test_parse_as_graph(file_edm_record_minimal):
    graph = Graph().parse(
        data=file_edm_record_minimal.decode("utf-8"),
        format="xml",
        publicID="placeholder",
    )

    aggregated = next(
        graph.objects(
            subject=URIRef("http://uri.test/edm#Aggregation"),
            predicate=URIRef("http://www.europeana.eu/schemas/edm/aggregatedCHO"),
        )
    )

    cho = next(
        graph.subjects(
            object=URIRef("http://www.europeana.eu/schemas/edm/ProvidedCHO"),
            predicate=URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),
        )
    )

    assert aggregated == cho
