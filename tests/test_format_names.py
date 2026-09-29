from lib.format_names import *

def test_pytest_setup_complete():
    assert True

def test_no_names():
    assert format_names([]) == ""

def test_one_name():
    assert format_names(["Bart"]) == "Bart"

def test_two_names():
    assert format_names(["Bart", "Lisa"]) == "Bart & Lisa"

def test_three_names():
    assert format_names(["Bart", "Lisa", "Maggie"]) == "Bart, Lisa & Maggie"

def test_four_names():
    assert format_names(["Bart", "Lisa", "Maggie", "Laurence"]) == "Bart, Lisa, Maggie & Laurence"