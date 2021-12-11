import ary
from ary.project import Project
import os
import pytest
import shutil

def setup_module(module):
    shutil.rmtree("tests/tmp/")
    os.mkdir("tests/tmp")

def test_add_file_from_template():
    project = Project("some_app", "test_lang", "and_author")
    ary.add_file_from_template("data/tests/foo.txt", "tests/tmp/foo.txt", project)
    assert(os.path.isfile("tests/tmp/foo.txt"))
    file = open("tests/tmp/foo.txt")
    text = file.read()
    assert(text == "some_app\ntest_lang\nand_author")