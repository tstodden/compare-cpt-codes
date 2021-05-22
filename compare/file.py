import hashlib
from typing import Dict, List

from .models import FileContent


class File:
    def __init__(self, file: FileContent):
        self._lines = self._initialize_lines(file.lines)

    @property
    def lines(self) -> Dict[str, str]:
        return self._lines

    def contains(self, hash_: str) -> bool:
        return hash_ in self._lines

    def _initialize_lines(self, lines: List[str]) -> Dict[str, str]:
        line_dict = dict()
        for ln in lines:
            hash_ = self._convert_line_to_hash(ln.strip())
            line_dict[hash_] = ln.strip()
        return line_dict

    def _convert_line_to_hash(self, line: str) -> str:
        byte = line.encode()
        return hashlib.sha1(byte).hexdigest()
