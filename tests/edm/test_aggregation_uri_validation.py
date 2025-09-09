import unittest
from pydantic import ValidationError
from edmlib import EDM_Parser, EDM_Record, EDM_ProvidedCHO, ORE_Aggregation, Ref, Lit
from rdflib import Graph, URIRef


class TestUmlautInUris(unittest.TestCase):
    def test_parse_xml(self):
        validation_errors = []

        try:
            record = EDM_Parser.from_string(
                """<?xml version="1.0" encoding="UTF-8"?>
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                xmlns:ore="http://www.openarchives.org/ore/terms/"
                xmlns:edm="http://www.europeana.eu/schemas/edm/"
                xmlns:dc="http://purl.org/dc/elements/1.1/">
                <edm:ProvidedCHO
                    rdf:about="https://uri.test/edm123ü">
                    <dc:type xml:lang="en">Text</dc:type>
                    <dc:title xml:lang="de">Titel</dc:title>
                    <dc:identifier>123</dc:identifier>
                    <dc:language>de</dc:language>
                    <edm:type>TEXT</edm:type>
                </edm:ProvidedCHO>
                <ore:Aggregation
                    rdf:about="http://uri.test/edm#Aggregation">
                    <edm:aggregatedCHO
                        rdf:resource="https://uri.test/edm123ü" />
                    <edm:dataProvider>Test</edm:dataProvider>
                    <edm:isShownAt
                        rdf:resource="http://uri.test/edm123.jpg" />
                    <edm:isShownBy
                        rdf:resource="http://uri.test/edm123.jpg" />
                    <edm:provider>Kulturpool</edm:provider>
                    <edm:rights rdf:resource="http://creativecommons.org/licenses/by-nc-sa/4.0/" />
                </ore:Aggregation>
            </rdf:RDF>
            """
            ).parse()
        except ValidationError as e:
            validation_errors.extend([error.get("msg") for error in e.errors()])

        self.assertNotIn(
            "Assertion failed, URIs of providedCHO and aggregation.edm_aggregatedCHO do not match: self.provided_cho.id.value='https://uri.test/edm123%C3%BC' != self.aggregation.edm_aggregatedCHO.value='https://uri.test/edm123ü'.",
            validation_errors,
        )

    def test_construct_programmatically(self):
        validation_errors = []

        try:
            record = EDM_Record(
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

        self.assertNotIn(
            "Assertion failed, URIs of providedCHO and aggregation.edm_aggregatedCHO do not match: self.provided_cho.id.value='https://uri.test/edm123%C3%BC' != self.aggregation.edm_aggregatedCHO.value='https://uri.test/edm123ü'.",
            validation_errors,
        )

    def test_parse_as_graph(self):
        graph = Graph().parse(
            data="""<?xml version="1.0" encoding="UTF-8"?>
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                xmlns:ore="http://www.openarchives.org/ore/terms/"
                xmlns:edm="http://www.europeana.eu/schemas/edm/"
                xmlns:dc="http://purl.org/dc/elements/1.1/">
                <edm:ProvidedCHO
                    rdf:about="https://uri.test/edm123ü">
                    <dc:type xml:lang="en">Text</dc:type>
                    <dc:title xml:lang="de">Titel</dc:title>
                    <dc:identifier>123</dc:identifier>
                    <dc:language>de</dc:language>
                    <edm:type>TEXT</edm:type>
                </edm:ProvidedCHO>
                <ore:Aggregation
                    rdf:about="http://uri.test/edm#Aggregation">
                    <edm:aggregatedCHO
                        rdf:resource="https://uri.test/edm123ü" />
                    <edm:dataProvider>Test</edm:dataProvider>
                    <edm:isShownAt
                        rdf:resource="http://uri.test/edm123.jpg" />
                    <edm:isShownBy
                        rdf:resource="http://uri.test/edm123.jpg" />
                    <edm:provider>Kulturpool</edm:provider>
                    <edm:rights rdf:resource="http://creativecommons.org/licenses/by-nc-sa/4.0/" />
                </ore:Aggregation>
            </rdf:RDF>
            """,
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

        self.assertEqual(aggregated, cho)
