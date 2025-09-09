from pytest import fixture
from pathlib import Path
import json


@fixture(scope="session")
def files():
    return Path(__file__).parent / "files"


@fixture(scope="session")
def cho_id_missmatch(files) -> dict:
    """Record is valid, but cho id has other value than ore-aggregation.aggregated_cho"""
    with open(files / "cho-id-missmatch.json", "rb") as file:
        return json.load(file)
