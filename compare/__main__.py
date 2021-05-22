import logging
import sys

from .comparer import FileComparer
from .controller import FileController
from .file import File


def validate(args: list) -> bool:
    is_valid = len(args) == 2
    return is_valid


args = sys.argv[1:]
if not validate(args):
    logging.fatal("Only two arguments are allowed")

controller = FileController()
old_file = File(controller.get_file(args[0]))
new_file = File(controller.get_file(args[1]))
comparer = FileComparer(old_file, new_file)
controller.write_file(comparer.compare())
