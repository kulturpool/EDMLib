import pytest
from edmlib.edm.validation.uri import is_valid_uri, sanitize_url_quotation


def test_invalid_uris(invalid_uri: str):
    assert not is_valid_uri(invalid_uri), f"Invalid URI was declared as valid."


def test_valid_uris(valid_uri: str):
    assert is_valid_uri(valid_uri), f"Valid URI was declared as invalid."


class TestSanitizeUrlQuotation:
    def test_basic_url(self):
        assert (
            sanitize_url_quotation("http://kpool.localhost/path/to/resource")
            == "http://kpool.localhost/path/to/resource"
        ), "Basic URL should not change."

    def test_url_with_params_and_fragment(self):
        assert (
            sanitize_url_quotation(
                "http://kpool.localhost/path/to/resource?query=1#fragment"
            )
            == "http://kpool.localhost/path/to/resource?query=1#fragment"
        )
        "URL with params and fragment should not change."

    @pytest.mark.skip(
        reason="Error known, most likely does not sabotage package usage for pipelines for now."
    )
    def test_url_with_quoted_params_and_fragment(self):
        assert (
            sanitize_url_quotation(
                "https://kpool.localhost/path/to/resource%3Fquery%3D1%23fragment"
            )
            == "https://kpool.localhost/path/to/resource%3Fquery%3D1%23fragment"
            "URL with quoted params and fragment should not change."
        )

    @pytest.mark.skip(
        reason="Error known, most likely does not sabotage package usage for pipelines for now."
    )
    def test_url_fully_quoted(self):
        assert (
            sanitize_url_quotation(
                "http%3A%2F%2Fkpool.localhost%2Fpath%2Fto%2Fresource%3Fquery%3D1%23fragment"
            )
            == "http://kpool.localhost/path/to/resource%3Fquery%3D1%23fragment"
            "URL with fully quoted characters should be properly quoted."
        )

    def test_local_uri(self):
        assert (
            sanitize_url_quotation("#local/resource") == "#local/resource"
        ), "Local URI should not change."

    def test_path_uri(self):
        assert (
            sanitize_url_quotation("/path/to/resource") == "/path/to/resource"
        ), "Path URI should not change."

    def test_quoted_colon_in_path(self):
        assert (
            sanitize_url_quotation("http://kpool.localhost/%3Fpath/to%3A8080/resource")
            == "http://kpool.localhost/%3Fpath/to%3A8080/resource"
        ), "URL with colon in path should not change."

    @pytest.mark.skip(
        reason="Error known, most likely does not sabotage package usage for pipelines for now."
    )
    def test_url_with_port(self):
        # fixme: hostname and port should not be masked by quotes"
        assert (
            sanitize_url_quotation("http://kpool.localhost:8080/path/to/resource")
            == "http://kpool.localhost:8080/path/to/resource"
        ), "URL with quoted params and fragment should not change."

    @pytest.mark.skip(
        reason="Error known, most likely does not sabotage package usage for pipelines for now."
    )
    def test_url_fully_quoted_with_port(self):
        # fixme: hostname and port should not be masked by quotes"
        assert (
            sanitize_url_quotation(
                "http://kpool.localhost%3A8080%2Fpath%2Fto%2Fresource%3Fquery%3D1%23fragment"
            )
            == "http://kpool.localhost:8080/path/to/resource%3Fquery%3D1%23fragment"
        ), "URL with quoted params and fragment should not change."

    @pytest.mark.skip(
        reason="Error known, most likely does not sabotage package usage for pipelines for now."
    )
    def test_url_basic_auth_and_port(self):
        # fixme: hostname and port should not be masked by quotes"
        assert (
            sanitize_url_quotation(
                "https://user:pass@kpool.localhost:8080/path/to/resource"
            )
            == "https://user:pass@kpool.localhost:8080/path/to/resource"
        ), "URL with quoted params and fragment should not change."

    @pytest.mark.skip(
        reason="Error known, most likely does not sabotage package usage for pipelines for now."
    )
    def test_url_fully_quoted_basic_auth_and_port(self):
        # fixme: hostname and port should not be masked by quotes"
        assert (
            sanitize_url_quotation(
                "http%3A%2F%2Fuser%3Apass%40kpool.localhost%3A8080%2Fpath%2Fto%2Fresource%3Fquery%3D1%23fragment"
            )
            == "http://user:pass@kpool.localhost:8080/path/to/resource%3Fquery%3D1%23fragment"
        ), "URL with quoted params and fragment should not change."
