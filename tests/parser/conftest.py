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
