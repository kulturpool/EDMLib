"""
This example returns a framed JSON-LD representation of an EDM record.

```
cd examples
poetry run python serialize_to_json_ld.py
```
"""

from edmlib import EDM_Parser
import json

if __name__ == "__main__":
    file = "minimal.xml"
    
    record = EDM_Parser.from_file(file).parse()
    jsonld = record.get_framed_json_ld()

    print((json.dumps(jsonld, indent=2)))

