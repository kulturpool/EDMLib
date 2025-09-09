from pytest import fixture
from pathlib import Path


@fixture(scope="session")
def files():
    return Path(__file__).parent / "files"


@fixture(scope="session")
def file_edm_record_minimal(files) -> bytes:
    with open(files / "edm-record-aggregation-uri.xml", "rb") as file:
        return file.read()


@fixture(scope="session")
def xml_with_lang_in_edm_type(files) -> bytes:
    with open(files / "xml-with-lang-in-edm-types.xml", "rb") as file:
        return file.read()


@fixture(scope="session")
def xml_with_xsdtypes(files) -> bytes:
    with open(files / "xml-with-xsdtypes.xml", "rb") as file:
        return file.read()


@fixture(scope="session")
def ref_lit_xml(files) -> bytes:
    with open(files / "ref-lit-xml.xml", "rb") as file:
        return file.read()


@fixture(scope="session")
def xml_with_empty_description(files) -> bytes:
    with open(files / "xml-with-empty-description.xml", "rb") as file:
        return file.read()


@fixture(scope="session")
def xml_with_empty_description_and_invalid_ref(files) -> bytes:
    with open(files / "xml-with-empy-description-and-invalid-ref.xml", "rb") as file:
        return file.read()
