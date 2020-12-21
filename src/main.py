import sys
import csv
import hashlib

class FileComparer:
    def __init__(self, args: list):
        self.oldFile = File(args[0])
        self.newFile = File(args[1])
        self.changedRows = []
    
    def compare(self):
        self.oldFile.convertFileRowsToDict()
        self.newFile.convertFileRowsToDict()
        for key in self.newFile.rowDict:
            self.appendRowIfDifferentInOldFile(key)
        self.writeDifferentRowsToOutput()

    def appendRowIfDifferentInOldFile(self, key: str):
        if self.isDifferentInOldFile(key):
            self.changedRows.append(self.newFile.rowDict[key])

    def writeDifferentRowsToOutput(self):
        with open("output.csv","w+") as outputCSV:
            csvWriter = csv.writer(outputCSV)
            csvWriter.writerows(self.changedRows)

    def isDifferentInOldFile(self, key: str) -> bool:
        isSame = key in self.oldFile.rowDict
        return not isSame

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

def validIfTwoArguments(args: list) -> bool:
    isValid = len(args) == 2
    return isValid

args = sys.argv[1:]
if validIfTwoArguments(args):
    comparer = FileComparer(args)
    comparer.compare()