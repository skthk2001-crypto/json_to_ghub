import json
import sys
from pathlib import Path


class LuaWriter:
    def __init__(self):
        self.lines = []

    def add(self, line=""):
        self.lines.append(line)

    def save(self, filename):
        Path(filename).write_text(
            "\n".join(self.lines),
            encoding="utf-8"
        )


def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def find_macro(data, name=None):
    """
    data가 배열이면 첫 번째 매크로나
    name과 같은 매크로를 찾는다.
    """

    if isinstance(data, list):

        if name:
            for item in data:
                if item.get("name") == name:
                    return item

        return data[0]

    return data


def get_components(macro):

    try:
        return macro["macro"]["sequence"]["toggleSequence"]["components"]

    except Exception:
        raise RuntimeError(
            "toggleSequence.components를 찾을 수 없습니다."
        )


def lua_value(v):

    if isinstance(v, bool):
        return "true" if v else "false"

    if v is None:
        return "nil"

    if isinstance(v, str):
        return '"' + v.replace('"', '\\"') + '"'

    return str(v)
