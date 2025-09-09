from pydantic import ValidationError
import pytest
from edmlib import EDM_Parser, EDM_Record, Ref
from pathlib import Path
from tests.fixtures.record import xml_string  # noqa: F401


def test_file_parser() -> None:
    ttl_path = Path(__file__).absolute().parent / "examples" / "ttl"
    ex_path = ttl_path / "output.ttl"

    parser = EDM_Parser.from_file(str(ex_path), format="ttl")
    assert parser
    rec = parser.parse()
    assert rec
    assert rec.provided_cho.id


def test_validation_edm_type_with_lang_raises(xml_with_lang_in_edm_type) -> None:
    with pytest.raises(ValidationError):
        parser = EDM_Parser.from_string(content=xml_with_lang_in_edm_type, format="xml")
        parser.parse()


def test_string_parser(xml_string) -> None:  # noqa: ANN001, F811
    parser = EDM_Parser.from_string(content=xml_string, format="xml")
    assert parser
    rec = parser.parse()
    assert rec
    assert EDM_Record.model_validate(rec)


def test_serialization_lit_ref(ref_lit_xml) -> None:
    parser = EDM_Parser.from_string(ref_lit_xml)
    rec = parser.parse()
    assert isinstance(rec.provided_cho.dc_type, list)
    assert len(rec.provided_cho.dc_type) == 1
    assert isinstance(rec.provided_cho.dc_type[0], Ref)
    dict_dump = rec.model_dump()

    re_rec = EDM_Record(**dict_dump)
    assert isinstance(re_rec.provided_cho.dc_type, list)
    assert len(re_rec.provided_cho.dc_type) == 1
    assert isinstance(re_rec.provided_cho.dc_type[0], Ref)


def test_xml_datatypes_parsing(xml_with_xsdtypes) -> None:
    parser = EDM_Parser.from_string(xml_with_xsdtypes)
    rec = parser.parse()
    assert rec


def test_parser_empty_element(xml_with_empty_description):
    parser = EDM_Parser.from_string(content=xml_with_empty_description, format="xml")
    rec = parser.parse()
    EDM_Record.model_validate(rec)
    assert (
        rec.provided_cho.dc_description is None
        or len(rec.provided_cho.dc_description) == 0
    )


def test_parser_empty_element_and_invalid_ref(
    xml_with_empty_description_and_invalid_ref,
):
    parser = EDM_Parser.from_string(
        content=xml_with_empty_description_and_invalid_ref, format="xml"
    )
    with pytest.raises(ValidationError):
        parser.parse()
