import csv
from csv_file import File

class FileComparer:
    def __init__(self, args: list):
        self.oldFile = File(args[0])
        self.newFile = File(args[1])
        self.changedRows = []
    
    def compare(self):
        self.convertOldAndNewFileRowsToDict()
        for key in self.newFile.rowDict:
            self.appendRowIfDifferentInOldFile(key)
        self.writeDifferentRowsToOutput()

    def convertOldAndNewFileRowsToDict(self):
        self.oldFile.convertFileRowsToDict()
        self.newFile.convertFileRowsToDict()

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