from rdflib import Graph
import os
from pathlib import Path
from edmlib.parser.edm_xml import EDM_Parser
from edmlib.edm import EDM_Record
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
    # test.provided_cho.id.value = "another_custom_value"
    dump = test.model_dump_json()

    with open(FILE / "test_1.json", "w") as file:
        file.write(dump)

    # Try restoring the EDM_Record from the json dump
    restored = EDM_Record(**json.loads(dump))
    # print(restored)

    print("dc_description: ", restored.provided_cho.dc_description)

    # Dump the restored EDM_Record object back to json.
    dump2 = restored.model_dump_json()
    with open(FILE / "restored_1.json", "w") as file:
        file.write(dump2)

    # Test creating a json schema from the EDM_Record model
    schema = EDM_Record.model_json_schema()
    with open(FILE / "schema.json", "w") as file:
        file.write(json.dumps(schema))

    # Test that Model can be turned into an rdf graph:
    restored_graph = restored.get_rdf_graph().serialize(FILE / "restored_graph.ttl", format="ttl")
