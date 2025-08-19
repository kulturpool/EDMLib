from edmlib.edm.value_types import Ref, Lit


def test_lit_normalization():
    lit = Lit(value="  Example Value  ")
    assert lit.value == "Example Value"


def test_ref_validation():
    ref = Ref(value="  https://example.com/resource  ")
    assert ref.value == "https://example.com/resource"
