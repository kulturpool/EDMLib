# ruff: noqa: F811

import unittest
import pytest
from tests.fixtures.uri import get_valid_uris, get_invalid_uris  # type:ignore # pylint: disable=import-error,unused-import # noqa: F401
from edmlib.edm.validation.uri import is_valid_uri, sanitize_url_quotation
from typing import Any


def test_invalid_uris(get_invalid_uris: Any):
    for sample in get_invalid_uris:
        assert not is_valid_uri(sample), f"Invalid uri {sample=} should be detected, but wasn't."


def test_valid_uris(get_valid_uris: Any):
    for sample in get_valid_uris:
        assert is_valid_uri(sample), f"Valid uri {sample=} should be allowed, but wasn't."


class SanitizeUrlQuotationTest(unittest.TestCase):
    def test_basic_url(self):
        self.assertEqual(
            sanitize_url_quotation("http://kpool.localhost/path/to/resource"),
            "http://kpool.localhost/path/to/resource",
            "Basic URL should not change.",
        )

    def test_url_with_params_and_fragment(self):
        self.assertEqual(
            sanitize_url_quotation("http://kpool.localhost/path/to/resource?query=1#fragment"),
            "http://kpool.localhost/path/to/resource?query=1#fragment",
            "URL with params and fragment should not change.",
        )

    def test_url_with_quoted_params_and_fragment(self):
        self.assertEqual(
            sanitize_url_quotation("https://kpool.localhost/path/to/resource%3Fquery%3D1%23fragment"),
            "https://kpool.localhost/path/to/resource%3Fquery%3D1%23fragment",
            "URL with quoted params and fragment should not change.",
        )

    def test_url_fully_quoted(self):
        self.assertEqual(
            sanitize_url_quotation("http%3A%2F%2Fkpool.localhost%2Fpath%2Fto%2Fresource%3Fquery%3D1%23fragment"),
            "http://kpool.localhost/path/to/resource%3Fquery%3D1%23fragment",
            "URL with fully quoted characters should be properly quoted.",
        )

    def test_local_uri(self):
        self.assertEqual(
            sanitize_url_quotation("#local/resource"),
            "#local/resource",
            "Local URI should not change.",
        )

    def test_path_uri(self):
        self.assertEqual(
            sanitize_url_quotation("/path/to/resource"),
            "/path/to/resource",
            "Path URI should not change.",
        )

    def test_quoted_colon_in_path(self):
        self.assertEqual(
            sanitize_url_quotation("http://kpool.localhost/%3Fpath/to%3A8080/resource"),
            "http://kpool.localhost/%3Fpath/to%3A8080/resource",
            "URL with colon in path should not change.",
        )

    @pytest.mark.skip(reason="no pass, fixme: hostname and port should not be masked by quotes")
    def test_url_with_port(self):
        self.assertEqual(
            sanitize_url_quotation("http://kpool.localhost:8080/path/to/resource"),
            "http://kpool.localhost:8080/path/to/resource",
            "URL with quoted params and fragment should not change.",
        )

    @pytest.mark.skip(reason="no pass, fixme: hostname and port should not be masked by quotes")
    def test_url_fully_quoted_with_port(self):
        self.assertEqual(
            sanitize_url_quotation("http://kpool.localhost%3A8080%2Fpath%2Fto%2Fresource%3Fquery%3D1%23fragment"),
            "http://kpool.localhost:8080/path/to/resource%3Fquery%3D1%23fragment",
            "URL with quoted params and fragment should not change.",
        )

    @pytest.mark.skip(reason="no pass, fixme: hostname and port should not be masked by quotes")
    def test_url_basic_auth_and_port(self):
        self.assertEqual(
            sanitize_url_quotation("https://user:pass@kpool.localhost:8080/path/to/resource"),
            "https://user:pass@kpool.localhost:8080/path/to/resource",
            "URL with quoted params and fragment should not change.",
        )

    @pytest.mark.skip(reason="no pass, fixme: hostname and port should not be masked by quotes")
    def test_url_fully_quoted_basic_auth_and_port(self):
        self.assertEqual(
            sanitize_url_quotation("http%3A%2F%2Fuser%3Apass%40kpool.localhost%3A8080%2Fpath%2Fto%2Fresource%3Fquery%3D1%23fragment"),
            "http://user:pass@kpool.localhost:8080/path/to/resource%3Fquery%3D1%23fragment",
            "URL with quoted params and fragment should not change.",
        )
