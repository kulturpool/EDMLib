from pytest import fixture
from pathlib import Path
from edmlib.edm import EDM_Record, EDM_ProvidedCHO, EDM_WebResource, ORE_Aggregation
import json


@fixture(scope="session")
def record_input_data() -> dict:
    with open(Path(__file__).parent / "record-input-data.json") as file:
        return json.load(file)


@fixture(scope="session")
def web_resource_input_data() -> dict:
    with open(Path(__file__).parent / "web-resource-input-data.json") as file:
        return json.load(file)


def test_provided_cho(record_input_data):
    assert EDM_ProvidedCHO(
        **record_input_data["provided_cho"]
    ), "Provided CHO init test failed"


def test_aggregation(record_input_data):
    assert ORE_Aggregation(
        **record_input_data["aggregation"]
    ), "Aggregation init test failed"


def test_webresource(web_resource_input_data):
    assert EDM_WebResource(**web_resource_input_data), "WebResource init test failed"


def test_record_init(record_input_data):
    assert (
        EDM_Record(**record_input_data).model_dump() == record_input_data
    ), "record input data did not equal parsed and re-serialised data"
