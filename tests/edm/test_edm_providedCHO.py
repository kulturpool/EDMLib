
from pydantic import ValidationError
import pytest
from edmlib.edm.classes.core import EDM_ProvidedCHO
from edmlib.edm.value_types import Lit, Ref

def test_providedcho_minimal_success():
    obj = EDM_ProvidedCHO(
        id=Ref(value="http://example.org/cho/1"),
        edm_type=Lit(value="IMAGE"),
        dc_description=[Lit(value="A description")],
        dc_language=[Lit(value="en")],
        dc_subject=[Lit(value="subject")],
        dc_title=[Lit(value="Title")],
        dc_type=[Lit(value="Type")],
        dc_identifier=[Lit(value="id123")]
    )
    assert obj.edm_type.value == "IMAGE"
    assert obj.dc_identifier[0].value == "id123"

def test_providedcho_missing_identifier_raises():
    with pytest.raises(ValidationError):
        EDM_ProvidedCHO(
            id=Ref(value="http://example.org/cho/2"),
            edm_type=Lit(value="IMAGE"),
            dc_description=[Lit(value="A description")],
            dc_language=[Lit(value="en")],
            dc_subject=[Lit(value="subject")],
            dc_title=[Lit(value="Title")],
            dc_type=[Lit(value="Type")]
        )

def test_providedcho_empty_identifier_raises():
    with pytest.raises(ValidationError):
        EDM_ProvidedCHO(
            id=Ref(value="http://example.org/cho/3"),
            edm_type=Lit(value="IMAGE"),
            dc_description=[Lit(value="A description")],
            dc_language=[Lit(value="en")],
            dc_subject=[Lit(value="subject")],
            dc_title=[Lit(value="Title")],
            dc_type=[Lit(value="Type")],
            dc_identifier=[Lit(value="")]
        )
