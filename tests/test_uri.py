# ruff: noqa: F811

from tests.fixtures.uri import get_valid_uris, get_invalid_uris  # type:ignore # pylint: disable=import-error,unused-import # noqa: F401
from edmlib.edm.validation.uri import is_valid_uri
from typing import Any


def test_invalid_uris(get_invalid_uris: Any):
    for sample in get_invalid_uris:
        assert not is_valid_uri(sample), f"Invalid uri {sample=} should be detected, but wasn't."


def test_valid_uris(get_valid_uris: Any):
    for sample in get_valid_uris:
        assert is_valid_uri(sample), f"Valid uri {sample=} should be allowed, but wasn't."
