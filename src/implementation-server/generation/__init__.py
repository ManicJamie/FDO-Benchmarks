import json
import os, pathlib
from glob import glob

from .internal_rep import FDO, generated

GEN_DIR = os.path.dirname(os.path.realpath(__file__))
OBJECT_DIR = os.path.join(GEN_DIR, "objects")

if not pathlib.Path(OBJECT_DIR).exists():  # Ensure target dir exists
    os.makedirs(OBJECT_DIR)

FDO_REGISTER: list[FDO] = []

def load():
    for obj in glob(OBJECT_DIR + "\\*.json"):
        with open(obj) as f:
            FDO_REGISTER.append(json.load(f))

def generate():
    """Generate 100 random FDOs. WARN: clears generation/objects directory!"""
    for file in glob(OBJECT_DIR + "\\*"):
        os.remove(file)
    
    for i in range(100):
        out = OBJECT_DIR + f"\\test_fdo_{i}.json"
        with open(out, "w") as file:
            json.dump(generated(i), file, indent=4)


if __name__ == "__main__":
    generate()

__all__ = ["FDO", "FDO_REGISTER", "load", "generate"]
