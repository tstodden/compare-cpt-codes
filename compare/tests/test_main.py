import unittest
from main import validIfTwoArguments

class TestValidArguments(unittest.TestCase):
    def testTwoArgumentsAreValid(self):
        args = ["file1.txt", "file2.txt"]

        isValid = validIfTwoArguments(args)

        self.assertTrue(isValid)

if __name__ == '__main__':
    unittest.main()