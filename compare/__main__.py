import sys
from .core import FileContent, File, FileComparer
from .services import FileController

def validIfTwoArguments(args: list) -> bool:
    isValid = len(args) == 2
    return isValid

args = sys.argv[1:]
if validIfTwoArguments(args):
    controller = FileController()
    oldFile = File(controller.getFileContent(args[0]))
    newFile = File(controller.getFileContent(args[1]))
    comparer = FileComparer(oldFile, newFile)
    controller.writeFileContent(comparer.compare())
