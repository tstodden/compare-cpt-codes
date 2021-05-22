from .file import File
from .models import FileContent

OUTPUT_FILE_NAME = "output.csv"


class FileComparer:
    def __init__(self, old_file: File, new_file: File):
        self.old_file = old_file
        self.new_file = new_file

    def compare(self) -> FileContent:
        changed_lines = list()
        for key, value in self.new_file.lines.items():
            if not self.old_file.contains(key):
                changed_lines.append(value + "\n")
        return FileContent(OUTPUT_FILE_NAME, changed_lines)
