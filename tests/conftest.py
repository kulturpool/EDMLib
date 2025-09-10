from pathlib import Path
from pytest import fixture


@fixture(scope="session")
def shared_files():
    return Path(__file__).parent / "conftest-files"


@fixture(scope="session")
def xml_string(shared_files) -> bytes:
    with open(shared_files / "xml-string.xml") as file:
        return file.read().encode("utf-8")
