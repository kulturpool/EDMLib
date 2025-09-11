from pydantic import ValidationError
import pytest
from edmlib import EDM_Parser, EDM_Record


def test_missing_edm_rights(get_record_with_missing_edm_rights):
    with pytest.raises(ValidationError):
        EDM_Parser.from_string(get_record_with_missing_edm_rights).parse()


def test_http_edm_rights(get_record_with_http_edm_rights):
    parser = EDM_Parser.from_string(get_record_with_http_edm_rights)
    assert isinstance(parser.parse(), EDM_Record)


def test_https_edm_rights(get_record_with_https_edm_rights):
    parser = EDM_Parser.from_string(get_record_with_https_edm_rights)
    assert isinstance(parser.parse(), EDM_Record)
