import json
from edm_python.edm import EDM_Record
from pathlib import Path

base = Path().absolute() / "conversion"

with open(base / "output/mmnoe/record_0.json", "r") as file:
    data = json.loads(file.read())


if __name__ == "__main__":
    edm = EDM_Record(**data["record"])
    print(edm)
