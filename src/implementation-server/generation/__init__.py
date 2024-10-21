
import dataclasses
import json
import os, pathlib
from glob import glob

from internal_rep import FDO

GEN_DIR = os.path.dirname(os.path.realpath(__file__))
OBJECT_DIR = os.path.join(GEN_DIR, "objects")


if not pathlib.Path(OBJECT_DIR).exists():  # Ensure target dir exists
    os.makedirs(OBJECT_DIR)


class DataclassJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)  # type:ignore
        return super().default(o)


FDO_REGISTER: dict[str, FDO] = {}

def load():
    object_files = [path for path in os.listdir(OBJECT_DIR) if path.endswith(".json")]

    for obj in object_files:
        with open(obj) as f:
            json.load(f)
            ...

def generate():
    """Generate 100 random FDOs. WARN: clears generation/objects directory!"""
    for f in glob(OBJECT_DIR + "\\*"):
        os.remove(f)
    
    for i in range(100):
        out = OBJECT_DIR + f"\\test_fdo_{i}.json"
        with open(out, "w") as f:
            json.dump(FDO.generated(i), f, indent=4, cls=DataclassJSONEncoder)


if __name__ == "__main__":
    generate()
