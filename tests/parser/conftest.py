from pytest import fixture
from pathlib import Path


@fixture(scope="session")
def files_edm():
    return Path(__file__).parent / "files"


@fixture(scope="session")
def file_edm_record_minimal(files_edm) -> bytes:
    with open(files_edm / "edm-record_aggregation-uri.xml", "rb") as file:
        return file.read()
