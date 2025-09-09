from edmlib import EDM_Parser
from tests.fixtures.record import xml_string
from pyld import jsonld


def test_json_ld_framing(xml_string):
    edm_record = EDM_Parser.from_string(xml_string).parse()
    framed = edm_record.get_framed_json_ld()
    assert framed
    flattened = jsonld.flatten(framed)
    assert flattened
    assert len(flattened) == 6


# test that validation of a record with missing co-dependent attributes in ore_Aggregation or edm_ProvidedCHO fails also when recovered from json!
