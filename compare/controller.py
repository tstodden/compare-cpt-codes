from .models import FileContent


class FileController:
    def get_file(self, filename: str) -> FileContent:
        with open(filename, 'r') as f:
            return FileContent(filename, f.readlines())

    def write_file(self, file: FileContent):
        with open(file.name, "w+") as f:
            f.writelines(file.lines)
