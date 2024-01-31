import json
import os
from pathlib import Path

filename = os.path.dirname(os.path.realpath(__file__))
filename += "\\data.json"

print(filename)

with open(Path(filename), "w") as f:
	json.dump({}, f)