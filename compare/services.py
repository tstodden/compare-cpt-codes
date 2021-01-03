from .core import FileContent

class FileController:
    def getFileContent(self, filename: str) -> FileContent:
        with open(filename,'r') as f:
            return FileContent(filename, f.readlines())

    def writeFileContent(self, fileContent: FileContent) -> bool:
        with open(fileContent.fileName,"w+") as f:
            f.writelines(fileContent.lines)
        return True
