import hashlib

OUTPUT_FILE_NAME = "output.csv"

class FileContent:
    fileName: str
    lines: [str]

    def __init__(self, _fileName: str, _lines: [str]):
        self.fileName = _fileName
        self.lines = _lines

class File:
    fileName: str
    lines: [str]
    lineDict: dict
    isConverted: bool

    def __init__(self, fileContent: FileContent):
        self.fileName = fileContent.fileName
        self.lines = fileContent.lines
        self.lineDict = dict()
        self.isConverted = False

    def getLineDict(self) -> dict:
        if (self.isConverted == False):
            self.convertFileLinesToDict()
            self.isConverted = True
        return self.lineDict

    def convertFileLinesToDict(self):
        for ln in self.getCleanLinesInFile():
            hash_ = self.convertStringToMD5Hash(ln)
            self.lineDict[hash_] = ln.split(sep=',')

    def getCleanLinesInFile(self) -> [str]:
        return list(map(str.strip, self.lines))
    
    def convertStringToMD5Hash(self, string: str) -> str:
        bytes_ = string.encode()
        return hashlib.md5(bytes_).hexdigest()

class FileComparer:
    previousFile: File
    currentFile: File

    def __init__(self, _previousFile: File, _currentFile: File):
        self.previousFile = _previousFile
        self.currentFile = _currentFile
    
    def compare(self) -> FileContent:
        lines = [self.currentFile.getLineDict()[key] for key in self.getDifferentKeys()]
        return FileContent(OUTPUT_FILE_NAME, lines)

    def getDifferentKeys(self) -> [str]:
        differentKeys = list()
        for key in self.currentFile.getLineDict():
            if self.isDifferentInPreviousFile(key):
                differentKeys.append(key)
        return differentKeys

    def isDifferentInPreviousFile(self, key: str) -> bool:
        isSame = key in self.previousFile.getLineDict()
        return not isSame
