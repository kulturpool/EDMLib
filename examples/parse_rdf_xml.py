"""
This example shows parsing a XML/RDF file into an edmlib record and print a
short summary table.


```
cd examples
poetry run python parse_rdf_xml.py minimal.xml
```
"""

import sys
from typing import get_type_hints
from edmlib import EDM_Parser, EDM_ProvidedCHO, ORE_Aggregation

if __name__ == "__main__":
    if len(sys.argv) != 2:
        if len(sys.argv) == 1:
            print("Error: No input file specified.")
        sys.exit(1)
    
    xml_file = sys.argv[1]
    
    record = EDM_Parser.from_file(xml_file).parse()

    print("\nEDM ProvidedCHO")
    print("-" * 15)

    for prop in get_type_hints(EDM_ProvidedCHO):
        attr = getattr(record.provided_cho, prop)
        if attr is not None:
            print(f"{prop:<20} | {str(attr)}")

    print("\nORE Aggregation")
    print("-" * 15)

    for prop in get_type_hints(ORE_Aggregation):
        attr = getattr(record.aggregation, prop)
        if attr is not None:
            print(f"{prop:<20} | {str(attr)}")

