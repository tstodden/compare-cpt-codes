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
    _lineDict: dict
    _isConverted: bool

    def __init__(self, fileContent: FileContent):
        self.fileName = fileContent.fileName
        self.lines = fileContent.lines
        self._lineDict = dict()
        self._isConverted = False

    def getLineDict(self) -> dict:
        if (self._isConverted == False):
            self._convertFileLinesToDict()
        return self._lineDict

    def _convertFileLinesToDict(self):
        for ln in self.lines:
            hash_ = self._convertStringToMD5Hash(ln.strip())
            self._lineDict[hash_] = ln
        self._isConverted = True
    
    def _convertStringToMD5Hash(self, string: str) -> str:
        bytes_ = string.encode()
        return hashlib.md5(bytes_).hexdigest()

class FileComparer:
    previousFile: File
    currentFile: File

    def __init__(self, _previousFile: File, _currentFile: File):
        self.previousFile = _previousFile
        self.currentFile = _currentFile
    
    def compare(self) -> FileContent:
        lines = [self.currentFile.getLineDict()[key] for key in self._getDifferentKeys()]
        return FileContent(OUTPUT_FILE_NAME, lines)

    def _getDifferentKeys(self) -> [str]:
        differentKeys = list()
        for key in self.currentFile.getLineDict():
            if self._isDifferentInPreviousFile(key):
                differentKeys.append(key)
        return differentKeys

    def _isDifferentInPreviousFile(self, key: str) -> bool:
        isSame = key in self.previousFile.getLineDict()
        return not isSame
