import os

from compare.comparer import OUTPUT_FILE_NAME, FileComparer
from compare.controller import FileController
from compare.file import File


class TestFileController():
    def test_comparing_two_files_with_one_difference(self):
        sut = FileController()
        old_file = File(sut.get_file("tests/data/old_file.txt"))
        new_file = File(sut.get_file("tests/data/new_file.txt"))
        comparer = FileComparer(old_file, new_file)
        content = comparer.compare()
        sut.write_file(content)

        with open(OUTPUT_FILE_NAME, "r") as f:
            got = f.readlines()
        os.remove(OUTPUT_FILE_NAME)

        want = ["23451,description\n"]
        assert got == want
