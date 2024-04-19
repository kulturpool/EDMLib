from rdflib import Graph
import json
from io import StringIO
import os
import pathlib
from edm_python.parsers import EDM_Parser

# output_dir = (
#     pathlib.Path().absolute().parent.parent.parent
#     / "code"
#     / "nhm"
#     / "kpool-backend"
#     / "sample_data"
# )
output_dir = pathlib.Path().absolute() / "conversion" / "output"
print(output_dir)
print(os.path.exists(output_dir))
# Output_dir = pathlib.Path("")


def process_json(idx, d, name):
    idx = idx
    header = d["header"]
    graph = Graph().parse(StringIO(json.dumps(d["metadata"])), format="json-ld")

    edm = EDM_Parser(graph).parse().model_dump_json()

    data = {"header": header, "record": json.loads(edm)}

    with open(f"{output_dir}/{name}/record_{idx}.json", "w") as file:
        file.write(json.dumps(data))
    # graph.serialize(f"conversion/output/{name}/graph_{idx}.ttl", encoding="ttl")


def process():
    for name in ["mmnoe", "albertina"]:
        if not os.path.exists(f"{output_dir}/{name}"):
            os.mkdir(f"{output_dir}/{name}")
            print("created dir", f"{output_dir}/{name}")
        with open(f"conversion/input/output_{name}.json", "r") as file:
            d = json.loads(file.read())

        for idx, el in enumerate(d):
            if idx % 1000 == 0:
                print("processing", name, idx)

            process_json(idx, el, name)
            break


if __name__ == "__main__":
    process()
