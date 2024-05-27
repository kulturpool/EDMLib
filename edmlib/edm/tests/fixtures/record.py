from pytest import fixture
from typing import Any
from edmlib.edm import EDM_Record


@fixture(scope="session")
def get_record():
    pass


@fixture(scope="session")
def valid_json_samples() -> list[dict[str, Any]]:
    return []


@fixture(scope="session")
def invalid_json_samples() -> list[dict[str, Any]]:
    return []


@fixture(scope="session")
def valid_record_samples() -> list[EDM_Record]:
    return []
