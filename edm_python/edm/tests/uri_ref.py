from pytest import raises
from edm_python.edm.tests.fixtures.uri import get_invalid_uris, get_valid_uris  # type:ignore # pylint: disable=import-error,unused-import # noqa: F401
from edm_python.edm.types import URIRefType
from pydantic import ValidationError
from typing import Any


def test_invalid_uriref_raises_exception(get_invalid_uris: Any):
    for invalid_uri in get_invalid_uris:
        with raises(ValidationError):
            URIRefType(value=invalid_uri)


def test_valid_uriref_passes_instanciation(get_valid_uris: Any):
    for valid_uri in get_valid_uris:
        assert URIRefType(value=valid_uri)
