from pytest import raises
from edmlib.edm.value_types import Ref
from pydantic import ValidationError


def test_invalid_uriref_raises_exception(invalid_uri):
    with raises(ValidationError):
        Ref(value=invalid_uri)


def test_valid_uriref_passes_instanciation(valid_uri):
    assert Ref(value=valid_uri)
