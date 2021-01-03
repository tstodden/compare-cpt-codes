import unittest
from compare.core import FileContent, File, FileComparer

TEST_DATA1 = "12345,description\n"
TEST_DATA2 = "67890,description\n"
TEST_DATA3 = "23451,description\n"

TEST_HASH1 = "51cbc4a28da5ca12cd0cfe8bf653f934"
TEST_HASH2 = "b2ca3638f7b2f5e0f3e7735d9c27569f"

class TestFile(unittest.TestCase):
    def test_converting_an_empty_file_to_a_dictionary(self):
        fileContent = FileContent("test.csv", [])
        sut = File(fileContent)

        result = sut.getLineDict()

        self.assertDictEqual({}, result)

    def test_converting_one_line_to_a_dictionary(self):
        fileContent = FileContent("test.csv", [TEST_DATA1])
        sut = File(fileContent)

        result = sut.getLineDict()

        self.assertDictEqual({TEST_HASH1:TEST_DATA1}, result)

    def test_converting_multiple_lines_to_a_dictionary(self):
        fileContent = FileContent("test.csv", [TEST_DATA1, TEST_DATA2])
        sut = File(fileContent)

        result = sut.getLineDict()

        self.assertDictEqual({TEST_HASH1:TEST_DATA1, TEST_HASH2:TEST_DATA2}, result)

class TestFileComparer(unittest.TestCase):
    def setUp(self):
        self.fileWithOneLine = File(
            FileContent("test.csv", [TEST_DATA1])
        )
        self.sameFileWithOneLine = File(
            FileContent("test.csv", [TEST_DATA1])
        )
        self.differentFileWithOneLine = File(
            FileContent("test.csv", [TEST_DATA3])
        )
        self.fileWithMultipleLines = File(
            FileContent("test.csv", [TEST_DATA1,TEST_DATA2])
        )
        self.sameFileWithMultipleLines = File(
            FileContent("test.csv", [TEST_DATA1,TEST_DATA2])
        )
        self.differentFileWithMultipleLines = File(
            FileContent("test.csv", [TEST_DATA3,TEST_DATA2])
        )

    def test_files_that_are_the_same_with_one_line(self):
        sut = FileComparer(self.fileWithOneLine, self.sameFileWithOneLine)

        result = sut.compare()

        self.assertEqual([], result.lines)

    def test_files_that_are_different_with_one_line(self):
        sut = FileComparer(self.fileWithOneLine, self.differentFileWithOneLine)

        result = sut.compare()

        self.assertEqual([TEST_DATA3], result.lines)

    def test_files_that_are_the_same_with_multiple_lines(self):
        sut = FileComparer(self.fileWithMultipleLines, self.sameFileWithMultipleLines)

        result = sut.compare()

        self.assertEqual([], result.lines)

    def test_files_that_are_different_with_multiple_lines(self):
        sut = FileComparer(self.fileWithMultipleLines, self.differentFileWithMultipleLines)

        result = sut.compare()

        self.assertEqual([TEST_DATA3], result.lines)
