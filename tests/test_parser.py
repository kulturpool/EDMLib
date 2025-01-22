from edmlib import EDM_Parser, EDM_Record
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


def test_string_parser(xml_string) -> None:  # noqa: ANN001, F811
    parser = EDM_Parser.from_string(content=xml_string, format="xml")
    assert parser
    rec = parser.parse()
    assert rec
    assert EDM_Record.model_validate(rec)
