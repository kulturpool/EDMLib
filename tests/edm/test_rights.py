from tests.fixtures.record import (
    get_record_with_http_edm_rights,
    get_record_with_https_edm_rights,
    get_record_with_missing_edm_rights,
)
from edmlib.edm.validation.edm_rights import assert_valid_statement
from edmlib import EDM_Parser, EDM_Record
from unittest import TestCase
from pydantic import ValidationError
import pytest


@pytest.mark.usefixtures("get_record_with_missing_edm_rights")
@pytest.mark.usefixtures("get_record_with_http_edm_rights")
@pytest.mark.usefixtures("get_record_with_https_edm_rights")
class EdmRightsTestCase(TestCase):
    def SetUp(self): ...

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, request):
        self.record_with_missing_rights = request.getfixturevalue(
            "get_record_with_missing_edm_rights"
        )
        self.record_with_https_rights = request.getfixturevalue(
            "get_record_with_https_edm_rights"
        )
        self.record_with_http_rights = request.getfixturevalue(
            "get_record_with_http_edm_rights"
        )

    def test_missing_edm_rights(self):
        parser = EDM_Parser.from_string(self.record_with_missing_rights)
        self.assertRaises(ValidationError, parser.parse)

    def test_http_edm_rights(self):
        parser = EDM_Parser.from_string(self.record_with_http_rights)
        self.assertIsInstance(parser.parse(), EDM_Record)


def test_for_valid_statements():
    statements = [
        # === creative commons 1.0 ===
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
    ]

    for statement in statements:
        assert_valid_statement(statement)


def test_for_invalid_statements():
    statements = [
        "http://other-commons.org/licenses/by/1.0/",
        "https://creativecommons.org/licenses/by-nc-nd/4.0/",
        "http://creativecommons.org/licenses/not-ok/4.0/",
    ]

    for statement in statements:
        with pytest.raises(AssertionError):
            assert_valid_statement(statement)
