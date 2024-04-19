from rdflib import Graph
import os
from pathlib import Path
from edm_python.parsers.edm_xml import EDM_Parser
from edm_python.edm import EDM_Record
import json

FILE = Path(__file__).absolute().parent


def process():
    graphs = [
        Graph().parse(FILE / "xml" / filename, format="xml")
        for filename in os.listdir(FILE / "xml")
        if filename.endswith("xml")
    ]
    return graphs


if __name__ == "__main__":
    graphs = process()
    test = EDM_Parser(graphs[0]).parse()
    dump = test.model_dump_json()

    with open(FILE / "test_1.json", "w") as file:
        file.write(dump)

    restored = EDM_Record(**json.loads(dump))
    print(restored)

    dump2 = restored.model_dump_json()

    with open(FILE / "restored_1.json", "w") as file:
        file.write(dump2)
