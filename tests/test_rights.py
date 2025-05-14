from tests.fixtures.record import (
    get_record_with_http_edm_rights,
    get_record_with_https_edm_rights,
    get_record_with_missing_edm_rights,
)
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
        self.record_with_https_rights = request.getfixturevalue("get_record_with_https_edm_rights")
        self.record_with_http_rights = request.getfixturevalue("get_record_with_http_edm_rights")

    def test_missing_edm_rights(self):
        parser = EDM_Parser.from_string(self.record_with_missing_rights)
        self.assertRaises(ValidationError, parser.parse)

    def test_http_edm_rights(self):
        parser = EDM_Parser.from_string(self.record_with_http_rights)
        self.assertIsInstance(parser.parse(), EDM_Record)

