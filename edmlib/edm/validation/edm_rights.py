import re

# order matters for non-greedy regex operator "|" below
creative_commons_licenses = [
    "mark",
    "zero",
    "by-nc-sa",
    "by-nc-nd",
    "by-nd",
    "by-nc",
    "by-sa",
    "by",
]

rights_statements_licenses = [
    "inc-nc",
    "inc-edu",
    "inc-ruu",
    "inc-ow-eu",
    "inc",
    "noc-oklr",
    "noc-us",
    "noc-cr",
    "noc-nc",
    "nkc",
    "cne",
    "und",
]

switch_pattern = re.compile(
    r"http://(www.)?(?P<host>creativecommons.org|rightsstatements.org)(?P<path>.*)"
)
creative_commons_pattern = re.compile(
    rf"/.*/(?P<license>{'|'.join(creative_commons_licenses)})"
)
rights_statements_pattern = re.compile(
    rf"/.*/(?P<license>{'|'.join(rights_statements_licenses)})"
)
creative_commons_normalize_pattern = re.compile(
    r"^(http://creativecommons.org/licenses/)(.+)(/[4]\.0/)(.+)$"
)


def normalize_statement(uri: str) -> str:
    normalized = uri.replace("https:", "http:").replace(
        "rightsstatements.org/page", "rightsstatements.org/vocab"
    )

    if creative_commons_normalize_pattern.match(normalized):
        # remove everything after version number (e.g. "/deed.de"), because "version
        # 4.0 discourages using ported versions and instead acts as a single global
        # license"
        normalized = creative_commons_normalize_pattern.sub(r"\1\2\3", normalized)

    return normalized


def assert_valid_statement(uri: str):
    match = switch_pattern.match(uri.lower())

    if not match:
        raise AssertionError(
            f"URI >{uri}< does neither match hostname >creativecommons.org< nor hostname >rightsstatements.org<."
        )

    hostname = match.group("host")
    path = match.group("path")

    match hostname:
        case "creativecommons.org":
            match = creative_commons_pattern.match(path)
            if not match:
                raise AssertionError(
                    f"URI >{uri}< does not match any of the creative commons licenses."
                )

        case "rightsstatements.org":
            match = rights_statements_pattern.match(path)
            if not match:
                raise AssertionError(
                    f"URI >{uri}< does not match any of the rights statements licenses."
                )
