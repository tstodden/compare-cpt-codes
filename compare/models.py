from typing import List, NamedTuple


class FileContent(NamedTuple):
    name: str
    lines: List[str]
