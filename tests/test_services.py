import os
import unittest
from compare.core import FileContent, File, FileComparer
from compare.services import FileController

PREVIOUS_CONTENT = "col1,col2\n12345,description\n67890,description"
CURRENT_CONTENT = "col1,col2\n23451,description\n67890,description"

class TestFileController(unittest.TestCase):
    def setUp(self):
        with open("tests/data/test-previous.csv", "w+") as f:
            f.writelines(PREVIOUS_CONTENT)
        with open("tests/data/test-current.csv", "w+") as f:
            f.writelines(CURRENT_CONTENT)
    
    def test_comparing_two_files_with_one_difference(self):
        sut = FileController()
        previousFile = File(sut.getFileContent("tests/data/test-previous.csv"))
        currentFile = File(sut.getFileContent("tests/data/test-current.csv"))
        comparer = FileComparer(previousFile, currentFile)
        results = comparer.compare()

        sut.writeFileContent(results)

        with open("output.csv", "r") as f:
            result = f.readlines()
        self.assertEqual(["23451,description\n"], result)
    
    def tearDown(self):
        os.remove("tests/data/test-previous.csv")
        os.remove("tests/data/test-current.csv")
        os.remove("output.csv")
