from pathlib import Path
from pytest import fixture


@fixture(scope="session")
def files():
    return Path(__file__).parent / "files"


@fixture(scope="session")
def xml_string(files) -> bytes:
    with open(files / "xml-string.xml") as file:
        return file.read().encode("utf-8")
