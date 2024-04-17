from edm_python.edm.tests.fixtures.record import (
    valid_json_samples,  # type:ignore # pylint: disable=import-error,unused-import # noqa: F401
    invalid_json_samples,  # type:ignore # pylint: disable=import-error,unused-import # noqa: F401
    valid_record_samples,  # type:ignore # pylint: disable=import-error,unused-import # noqa: F401
)
from typing import Any


def test_valid_json_instantiation(valid_json_samples: Any):
    # assert that you can instanciate an EDM_Record from each valid json
    for sample in valid_json_samples:
        print(sample)
    pass


def test_invalid_json_instantiation(invalid_json_samples: Any):
    # assert that you cannot instanciate an EDM_Record from each invalid json
    for sample in invalid_json_samples:
        print(sample)
    pass


def test_valid_record_recovery(valid_record_samples: Any):
    # dump the record to json

    # assert that you can instanciate an EDM_Record form the dumped json
    for sample in valid_record_samples:
        print(sample)
    pass


# test that validation of a record with missing co-dependent attributes in ore_Aggregation or edm_ProvidedCHO fails also when recovered from json!
