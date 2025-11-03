import json
from pathlib import Path

def getList(path:str):
    data_path = Path(__file__).parent / path
    try:
        with data_path.open(encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise SystemExit(f"JSON file not found: {data_path}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"Invalid JSON: {e}")

    if isinstance(data, list):
        return data
    else:
        raise SystemExit("Unexpected JSON structure in " + str(data_path))