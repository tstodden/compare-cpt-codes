from compare.comparer import OUTPUT_FILE_NAME, FileComparer
from compare.file import File
from compare.models import FileContent

TEST_DATA1 = "12345,description\n"
TEST_DATA2 = "67890,description\n"
TEST_DATA3 = "23451,description\n"

TEST_HASH1 = "a587b9ca9c40faade4d867e6a72109fc38312d45"
TEST_HASH2 = "65c26c9c3d3cf8935623c50ac99fe5322acb52a3"


class TestFile():
    def test_converting_an_empty_file_to_a_dictionary(self):
        content = FileContent("test.csv", [])
        sut = File(content)

        got = sut.lines

        want = {}
        assert got == want

    def test_converting_one_line_to_a_dictionary(self):
        content = FileContent("test.csv", [TEST_DATA1])
        sut = File(content)

        got = sut.lines

        want = {TEST_HASH1: TEST_DATA1.strip()}
        assert got == want

    def test_converting_multiple_lines_to_a_dictionary(self):
        content = FileContent("test.csv", [TEST_DATA1, TEST_DATA2])
        sut = File(content)

        got = sut.lines

        want = {TEST_HASH1: TEST_DATA1.strip(), TEST_HASH2: TEST_DATA2.strip()}
        assert got == want


class TestFileComparer():
    def test_files_that_are_the_same_with_one_line(self):
        file_with_one_line = File(FileContent("test.csv", [TEST_DATA1]))
        same_file = File(FileContent("test.csv", [TEST_DATA1]))
        sut = FileComparer(file_with_one_line, same_file)

        got = sut.compare()

        want = FileContent(OUTPUT_FILE_NAME, [])
        assert got == want

    def test_files_that_are_different_with_one_line(self):
        file_with_one_line = File(FileContent("test.csv", [TEST_DATA1]))
        different_file = File(FileContent("test.csv", [TEST_DATA3]))
        sut = FileComparer(file_with_one_line, different_file)

        got = sut.compare()

        want = FileContent(OUTPUT_FILE_NAME, [TEST_DATA3])
        assert got == want

    def test_files_that_are_the_same_with_multiple_lines(self):
        file_with_multiple_lines = File(
            FileContent("test.csv", [TEST_DATA1, TEST_DATA2])
        )
        same_file = File(
            FileContent("test.csv", [TEST_DATA1, TEST_DATA2])
        )
        sut = FileComparer(file_with_multiple_lines, same_file)

        got = sut.compare()

        want = FileContent(OUTPUT_FILE_NAME, [])
        assert got == want

    def test_files_that_are_different_with_multiple_lines(self):
        file_with_multiple_lines = File(
            FileContent("test.csv", [TEST_DATA1, TEST_DATA2])
        )
        different_file = File(
            FileContent("test.csv", [TEST_DATA3, TEST_DATA2])
        )
        sut = FileComparer(file_with_multiple_lines, different_file)

        got = sut.compare()

        want = FileContent(OUTPUT_FILE_NAME, [TEST_DATA3])
        assert got == want
