import csv
from .core import FileContent

class FileController:
    def getFileContent(self, filename: str) -> FileContent:
        with open(filename, 'r') as f:
            return FileContent(filename, f.readlines())

    def writeFileContent(self, fileContent: FileContent) -> bool:
        with open(fileContent.fileName,"w+") as f:
            csvWriter = csv.writer(f)
            csvWriter.writerows(fileContent.lines)
        return True
