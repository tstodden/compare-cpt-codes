from src.main import validIfTwoArguments

def testIsValidWithTwoArguments():
    args = ["file1", "file2"]

    isValid = validIfTwoArguments(args)

    assert isValid == True