from edmlib import EDM_Parser, EDM_Record, Ref, Lit
from pathlib import Path
from tests.fixtures.record import xml_string  # noqa: F401
from tests.fixtures.parser import get_ref_lit_json, get_ref_lit_xml


def test_file_parser() -> None:
    ttl_path = Path(__file__).absolute().parent / "examples" / "ttl"
    ex_path = ttl_path / "output.ttl"

    parser = EDM_Parser.from_file(str(ex_path), format="ttl")
    assert parser
    rec = parser.parse()
    assert rec
    assert rec.provided_cho.id


def test_string_parser(xml_string) -> None:  # noqa: ANN001, F811
    parser = EDM_Parser.from_string(content=xml_string, format="xml")
    assert parser
    rec = parser.parse()
    assert rec
    assert EDM_Record.model_validate(rec)


def test_serialization_lit_ref(get_ref_lit_xml) -> None:
    parser = EDM_Parser.from_string(get_ref_lit_xml)
    rec = parser.parse()
    assert isinstance(rec.provided_cho.dc_type, list)
    assert len(rec.provided_cho.dc_type) == 1
    assert isinstance(rec.provided_cho.dc_type[0], Ref)
    dict_dump = rec.model_dump()

    re_rec = EDM_Record(**dict_dump)
    assert isinstance(re_rec.provided_cho.dc_type, list)
    assert len(re_rec.provided_cho.dc_type) == 1
    assert isinstance(re_rec.provided_cho.dc_type[0], Ref)
