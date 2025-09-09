import pytest
from edmlib import EDM_Parser
from edmlib.edm.classes.core import EDM_ProvidedCHO

MINIMAL_EDM_XML_WITH_OWLSAMEAS = '''<?xml version="1.0"?>
<rdf:RDF
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:edm="http://www.europeana.eu/schemas/edm/"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:owl="http://www.w3.org/2002/07/owl#"
    xmlns:ore="http://www.openarchives.org/ore/terms/"
>
  <edm:ProvidedCHO rdf:about="http://example.org/cho/1">
    <edm:type>IMAGE</edm:type>
    <dc:identifier>id-1</dc:identifier>
    <dc:description>Test object</dc:description>
    <dc:subject>Test subject</dc:subject>
    <dc:title>Test title</dc:title>
    <dc:language>en</dc:language>
    <dc:type>TestType</dc:type>
    <dcterms:spatial xmlns:dcterms="http://purl.org/dc/terms/">TestPlace</dcterms:spatial>
    <dcterms:temporal xmlns:dcterms="http://purl.org/dc/terms/">TestTime</dcterms:temporal>
    <owl:sameAs rdf:resource="http://example.org/other/1"/>
    <owl:sameAs rdf:resource="http://example.org/other/2"/>
  </edm:ProvidedCHO>
  <ore:Aggregation rdf:about="http://example.org/aggr/1">
    <edm:aggregatedCHO rdf:resource="http://example.org/cho/1"/>
    <edm:dataProvider>Test DataProvider</edm:dataProvider>
    <edm:provider>Test Provider</edm:provider>
    <edm:rights rdf:resource="http://rightsstatements.org/vocab/InC/1.0/"/>
    <edm:isShownAt rdf:resource="http://example.org/view/1"/>
    <edm:isShownBy rdf:resource="http://example.org/image/1"/>
  </ore:Aggregation>
</rdf:RDF>
'''

def test_parser_owl_sameas():
    parser = EDM_Parser.from_string(MINIMAL_EDM_XML_WITH_OWLSAMEAS, format="xml")
    record = parser.parse()
    cho: EDM_ProvidedCHO = record.provided_cho

    # Only accept 'owl_sameAs' as the correct attribute name
    sameas = cho.owl_sameAs
    assert sameas is not None, "owl:sameAs property not parsed (expected attribute 'owl_sameAs')"

    # Require a list of two values
    assert isinstance(sameas, list), f"owl_sameAs should be a list, got {type(sameas)}"
    assert len(sameas) == 2, f"Expected 2 owl:sameAs, got {len(sameas)}"

    uris = {ref.value for ref in sameas}
    assert "http://example.org/other/1" in uris, "Missing first owl:sameAs URI"
    assert "http://example.org/other/2" in uris, "Missing second owl:sameAs URI"
