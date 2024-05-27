from pytest import fixture


@fixture(scope="session")
def get_invalid_uris() -> list[str]:
    # TODO: check that this are all really invalid
    return [
        "http://www.example.com/path with spaces",
        "http://www.example.com/query?name=John Doe",
        # "htp://www.example.com",
        # "http://www.example.com/über",
        "/path/to/resource",
        # "http://www.example",
        # "http://www.ex*mple.com",
        "http://www.exmple.com/{I}nvalid",
        # "file:///path/to/resource",
        # "http://www.example.com:abc",
        "http://www.example.com/control^characters",
        "http://www.example.com/path/<resource>",
        "#local_identifier",
    ]


@fixture(scope="session")
def get_valid_uris() -> list[str]:
    return [
        "http://www.example.com/search?q=example",
        "http://www.example.com/page#section1",
        "http://192.0.2.1",
        "myapp://open?id=123",
        "http://www.example.com:8080",
        "http://www.example.com/%20encoded%20path",
        "ftp://username:password@ftp.example.com",
        "urn:sample-institution/ObjectID",
        "ftp://username:password@ftp.example.com",
    ]


@fixture(scope="session")
def get_uris_with_invalid_encoding() -> list[str]:
    return [""]
