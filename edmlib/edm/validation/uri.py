# pylint: disable=pointless-string-statement
from rdflib.term import _is_valid_uri
from edmlib.edm.exceptions import InvalidRefException

"""
This is the function that validates a URIRef in rdflib:

_invalid_uri_chars = '<>" {}|\\^`'


def _is_valid_uri(uri: str) -> bool:
    for c in _invalid_uri_chars:
        if c in uri:
            return False
    return True

    

## This is how a uriref is instanciated (it uses the class __new__): 

def __new__(cls, value: str, base: Optional[str] = None) -> "URIRef":
    if base is not None:
        ends_in_hash = value.endswith("#")
        # type error: Argument "allow_fragments" to "urljoin" has incompatible type "int"; expected "bool"
        value = urljoin(base, value, allow_fragments=1)  # type: ignore[arg-type]
        if ends_in_hash:
            if not value.endswith("#"):
                value += "#"

    if not _is_valid_uri(value):
        logger.warning(
            "%s does not look like a valid URI, trying to serialize this will break."
            % value
        )

    try:
        rt = str.__new__(cls, value)
    except UnicodeDecodeError:
        # type error: No overload variant of "__new__" of "str" matches argument types "Type[URIRef]", "str", "str"
        rt = str.__new__(cls, value, "utf-8")  # type: ignore[call-overload]
    return rt

TODO: I think this is not enough for our case. it does not catch local uris.

"""


def uri_is_not_local(uri: str) -> bool:
    return not uri.startswith("#")


def uri_is_not_path(uri: str) -> bool:
    return not uri.startswith("/")


def is_valid_uri(uri: str, strict: bool = False) -> bool:
    """
    Validate that an uri conforms to the definition.

    Returns bool by default.
    If strict = True -> will raise an InvalidURIRefException.
    """
    if _is_valid_uri(uri) and uri_is_not_local(uri) and uri_is_not_path(uri):
        return True
    elif strict:
        raise InvalidRefException(f"Uri is invalid: '{uri}'.")
    else:
        return False
