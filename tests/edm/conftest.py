from pytest import fixture, FixtureRequest
from pathlib import Path
import json


@fixture(scope="session")
def core_files():
    return Path(__file__).parent / "files"


@fixture(scope="session")
def cho_id_missmatch(core_files) -> dict:
    """Record is valid, but cho id has other value than ore-aggregation.aggregated_cho"""
    with open(core_files / "cho-id-missmatch.json", "rb") as file:
        return json.load(file)


@fixture(
    scope="session",
    params=[
        # "http://www.example.com/path with spaces",
        # "http://www.example.com/query?name=John Doe",
        # "htp://www.example.com",
        # "http://www.example.com/über",
        "/path/to/resource",
        # "http://www.example",
        # "http://www.ex*mple.com",
        # "http://www.exmple.com/{I}nvalid",
        # "file:///path/to/resource",
        # "http://www.example.com:abc",
        # "http://www.example.com/control^characters",
        # "http://www.example.com/path/<resource>",
        "#local_identifier",
    ],
)
def invalid_uri(request: FixtureRequest) -> str:
    return request.param


@fixture(
    scope="session",
    params=[
        "http://www.example.com/search?q=example",
        "http://www.example.com/page#section1",
        "http://192.0.2.1",
        "myapp://open?id=123",
        "http://www.example.com:8080",
        "http://www.example.com/%20encoded%20path",
        "ftp://username:password@ftp.example.com",
        "urn:sample-institution/ObjectID",
        "ftp://username:password@ftp.example.com",
    ],
)
def valid_uri(request: FixtureRequest) -> str:
    return request.param
