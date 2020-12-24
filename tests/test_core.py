import unittest
from compare.core import FileContent, File, FileComparer

class TestFile(unittest.TestCase):
    def test_converting_an_empty_file_to_a_dictionary(self):
        fileContent = FileContent("test.csv", [])
        sut = File(fileContent)

        lineDict = sut.getLineDict()

        self.assertDictEqual({}, lineDict)

    def test_converting_one_line_to_a_dictionary(self):
        fileContent = FileContent("test.csv", ["12345,description"])
        sut = File(fileContent)

        lineDict = sut.getLineDict()

        self.assertDictEqual(
            {"51cbc4a28da5ca12cd0cfe8bf653f934":["12345","description"]},
            lineDict
        )

    def test_converting_multiple_lines_to_a_dictionary(self):
        fileContent = FileContent(
            "test.csv",
            ["12345,description\n", "67890,description"]
        )
        sut = File(fileContent)

        lineDict = sut.getLineDict()

        self.assertDictEqual(
            {
                "51cbc4a28da5ca12cd0cfe8bf653f934":["12345","description"],
                "b2ca3638f7b2f5e0f3e7735d9c27569f":["67890","description"]
            },
            lineDict
        )

class TestFileComparer(unittest.TestCase):
    def setUp(self):
        self.fileWithOneLine = File(
            FileContent("test.csv",["12345,description"])
        )
        self.sameFileWithOneLine = File(
            FileContent("test.csv",["12345,description"])
        )
        self.differentFileWithOneLine = File(
            FileContent("test.csv",["23451,description"])
        )
        self.fileWithMultipleLines = File(
            FileContent("test.csv",["12345,description\n","67890,description"])
        )
        self.sameFileWithMultipleLines = File(
            FileContent("test.csv",["12345,description\n","67890,description"])
        )
        self.differentFileWithMultipleLines = File(
            FileContent("test.csv",["23451,description\n","67890,description"])
        )

    def test_files_that_are_the_same_with_one_line(self):
        sut = FileComparer(self.fileWithOneLine, self.sameFileWithOneLine)

        delta = sut.compare()

        self.assertEqual([], delta.lines)

    def test_files_that_are_different_with_one_line(self):
        sut = FileComparer(self.fileWithOneLine, self.differentFileWithOneLine)

        delta = sut.compare()

        self.assertEqual([["23451","description"]], delta.lines)

    def test_files_that_are_the_same_with_multiple_lines(self):
        sut = FileComparer(self.fileWithMultipleLines, self.sameFileWithMultipleLines)

        delta = sut.compare()

        self.assertEqual([], delta.lines)

    def test_files_that_are_different_with_multiple_lines(self):
        sut = FileComparer(self.fileWithMultipleLines, self.differentFileWithMultipleLines)

        delta = sut.compare()

        self.assertEqual([["23451","description"]], delta.lines)
