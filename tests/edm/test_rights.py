from edmlib.edm.validation.edm_rights import assert_valid_statement
import pytest


@pytest.mark.parametrize(
    "statement",
    [
        "http://creativecommons.org/licenses/by/1.0/",
        "http://creativecommons.org/licenses/by-sa/1.0/fi/",
        "http://creativecommons.org/licenses/by-nd/1.0/il/",
        "http://creativecommons.org/licenses/by-nc/1.0/nl/",
        "http://creativecommons.org/licenses/by-nc-sa/1.0/nl/",
        "http://creativecommons.org/licenses/by-nd-nc/1.0/nl/",
        # === creative commons 2.0 ===
        "http://creativecommons.org/licenses/by/2.0/",
        "http://creativecommons.org/licenses/by-sa/2.0/au/",
        "http://creativecommons.org/licenses/by-nd/2.0/at/",
        "http://creativecommons.org/licenses/by-nc/2.0/be/",
        "http://creativecommons.org/licenses/by-nc-sa/2.0/br/",
        "http://creativecommons.org/licenses/by-nc-nd/2.0/ca/",
        # === creative commons 3.0 ===
        "http://creativecommons.org/licenses/by/3.0/",
        "http://creativecommons.org/licenses/by-sa/3.0/au/",
        "http://creativecommons.org/licenses/by-nd/3.0/at/",
        "http://creativecommons.org/licenses/by-nc/3.0/br/",
        "http://creativecommons.org/licenses/by-nc-sa/3.0/cl/",
        "http://creativecommons.org/licenses/by-nc-nd/3.0/cn/",
        # === creative commons 4.0 ===
        "http://creativecommons.org/licenses/by/4.0/",
        "http://creativecommons.org/licenses/by-sa/4.0/",
        "http://creativecommons.org/licenses/by-nd/4.0/",
        "http://creativecommons.org/licenses/by-nc/4.0/",
        "http://creativecommons.org/licenses/by-nc-sa/4.0/",
        "http://creativecommons.org/licenses/by-nc-nd/4.0/",
    ],
)
def test_for_valid_statements(statement):
    assert_valid_statement(statement)


@pytest.mark.parametrize(
    "statement",
    [
        "http://other-commons.org/licenses/by/1.0/",
        "https://creativecommons.org/licenses/by-nc-nd/4.0/",
        "http://creativecommons.org/licenses/not-ok/4.0/",
    ],
)
def test_for_invalid_statements(statement):
    with pytest.raises(AssertionError):
        assert_valid_statement(statement)
