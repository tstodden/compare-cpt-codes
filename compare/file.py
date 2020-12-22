import hashlib

class File:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.rawRows = f.readlines()
        self.rowDict = {}

    def convertFileRowsToDict(self):
        self.cleanRowsInFile()
        for row in self.rawRows:
            hash_ = self.convertRowToMD5Hash(row)
            self.rowDict[hash_] = row.split(sep=',')

    def cleanRowsInFile(self):
        cleanRows = []
        for row in self.rawRows:
            cleanRows.append(row.strip())
        self.rawRows = cleanRows
    
    def convertRowToMD5Hash(self, row: str) -> str:
        bytes_ = row.encode()
        hash_ = hashlib.md5(bytes_)
        return hash_.hexdigest()