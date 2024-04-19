import os
from pathlib import Path
import json
from rdflib import Graph

FILE = Path(__file__).absolute().parent
XML = FILE / "xml"


def process():
    with open(FILE / "framed" / "output_mmnoe.json", "r") as file:
        data = json.loads(file.read())[500:511]

    for idx, el in enumerate(data):
        with open(FILE / "framed" / "records" / f"framed_{idx}.json", "w") as file:
            file.write(json.dumps(el["metadata"]))

    for idx, el in enumerate(
        list(
            filter(
                lambda x: x.endswith(".json"), os.listdir(FILE / "framed" / "records")
            )
        )
    ):
        g = Graph().parse(FILE / "framed" / "records" / el)
        g.serialize(XML / f"rec_{idx}.xml", format="pretty-xml")


if __name__ == "__main__":
    print()
    process()
