from pytest import fixture
from pathlib import Path


def _get_bytes(path: Path) -> bytes:
    with open(path, "rb") as file:
        return file.read()


@fixture(scope="session")
def parser_files():
    return Path(__file__).parent / "files"


@fixture(scope="session")
def file_edm_record_minimal(parser_files) -> bytes:
    return _get_bytes(parser_files / "edm-record-aggregation-uri.xml")


@fixture(scope="session")
def xml_with_lang_in_edm_type(parser_files) -> bytes:
    return _get_bytes(parser_files / "xml-with-lang-in-edm-types.xml")


@fixture(scope="session")
def xml_with_xsdtypes(parser_files) -> bytes:
    return _get_bytes(parser_files / "xml-with-xsdtypes.xml")


@fixture(scope="session")
def ref_lit_xml(parser_files) -> bytes:
    return _get_bytes(parser_files / "ref-lit-xml.xml")


@fixture(scope="session")
def xml_with_empty_description(parser_files) -> bytes:
    return _get_bytes(parser_files / "xml-with-empty-description.xml")


@fixture(scope="session")
def xml_with_empty_description_and_invalid_ref(parser_files) -> bytes:
    return _get_bytes(parser_files / "xml-with-empy-description-and-invalid-ref.xml")


@fixture(scope="session")
def xml_with_gyear(parser_files) -> bytes:
    return _get_bytes(parser_files / "xml-with-gyear.xml")


@fixture(scope="session")
def get_record_with_missing_edm_rights(parser_files) -> bytes:
    return _get_bytes(parser_files / "record-with-missing-edm-rights.xml")


@fixture(scope="session")
def get_record_with_https_edm_rights(parser_files) -> bytes:
    return _get_bytes(parser_files / "record-with-https-edm-rights.xml")


@fixture(scope="session")
def get_record_with_http_edm_rights(parser_files) -> bytes:
    return _get_bytes(parser_files / "record-with-http-edm-rights.xml")
