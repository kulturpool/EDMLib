# ruff: noqa: F811

from edmlib.parser.edm_xml import EDM_Parser
from tests.fixtures.record import (
    valid_json_samples,  # type:ignore # pylint: disable=import-error,unused-import # noqa: F401
    invalid_json_samples,  # type:ignore # pylint: disable=import-error,unused-import # noqa: F401
    valid_record_samples,  # type:ignore # pylint: disable=import-error,unused-import # noqa: F401
    xml_string,
)
from typing import Any
from pyld import jsonld


def test_valid_json_instantiation(valid_json_samples: list[dict[str, Any]]) -> None:
    # assert that you can instanciate an EDM_Record from each valid json
    for sample in valid_json_samples:
        print(sample)
    pass


def test_invalid_json_instantiation(invalid_json_samples: list[dict[str, Any]]) -> None:
    # assert that you cannot instanciate an EDM_Record from each invalid json
    for sample in invalid_json_samples:
        print(sample)
    pass


def test_valid_record_recovery(valid_record_samples: list[dict[str, Any]]) -> None:
    # dump the record to json

    # assert that you can instanciate an EDM_Record form the dumped json
    for sample in valid_record_samples:
        print(sample)
    pass


def test_json_ld_framing(xml_string):
    edm_record = EDM_Parser.from_string(xml_string).parse()
    framed = edm_record.get_framed_json_ld()
    assert framed
    flattened = jsonld.flatten(framed)
    assert flattened
    assert len(flattened) == 6


# test that validation of a record with missing co-dependent attributes in ore_Aggregation or edm_ProvidedCHO fails also when recovered from json!


def test_minimal_record() -> None:
    # TODO: test that all variants of minimal viable records are passing validation
    pass
