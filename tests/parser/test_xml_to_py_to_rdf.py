from edmlib import EDM_Parser


def test_gyear_serialization_cycle(xml_with_gyear):
    parser = EDM_Parser.from_string(xml_with_gyear)
    first_rec = parser.parse()

    xml_from_rec = first_rec.serialize()
    parser = EDM_Parser.from_string(xml_from_rec)
    second_rec = parser.parse()

    assert second_rec.edm_agent and second_rec.edm_agent[0]
    assert second_rec.edm_agent[0].rdagr2_dateOfBirth
    assert str(second_rec.edm_agent[0].rdagr2_dateOfBirth.value) == "1885"
