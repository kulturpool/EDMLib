from edmlib.edm.value_types import Lit


EDM_TYPES = {"TEXT", "VIDEO", "SOUND", "IMAGE", "3D"}


def assert_valid_edm_type(edm_type: Lit):
    assert (
        edm_type.value in EDM_TYPES
    ), f"Provided edm_type must be one of {EDM_TYPES}, got {edm_type.value=}."
