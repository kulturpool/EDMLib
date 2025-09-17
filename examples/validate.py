"""
This example parses an invalid edmlib record and prints validation errors.

```
cd examples
poetry run python validate.py
```
"""

from pydantic import ValidationError
from edmlib import EDM_Parser

if __name__ == "__main__":
    file = "invalid.xml"
    
    try:
        record = EDM_Parser.from_file(file).parse()
    except ValidationError as why:
        print(f"Validation errors found in {file}:")

        for e in why.errors():
            print(f"- {e.get("msg")}")

