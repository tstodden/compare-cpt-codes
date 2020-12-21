import sys
from file_comparer import FileComparer

def validIfTwoArguments(args: list) -> bool:
    isValid = len(args) == 2
    return isValid

args = sys.argv[1:]
if validIfTwoArguments(args):
    comparer = FileComparer(args)
    comparer.compare()