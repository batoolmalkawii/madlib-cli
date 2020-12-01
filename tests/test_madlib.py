from madlib_cli.madlib import read_template
from madlib_cli.madlib import parse
from madlib_cli.madlib import merge

"""
**read_templeate** test cases:
1. "" -> ""
2. "Hello there, this is Batool." -> "Hello there, this is Batool."
3. "Hello there, this is {Name}, I am {Age} years old." -> "Hello there, this is {Name}, I am {Age} years old."
"""
def test_read_empty():
    actual = read_template("assets/test_empty.txt")
    expected = ""
    assert actual == expected

def test_read_no_placeholders():
    actual = read_template("assets/test_no_placeholders.txt")
    expected = "Hello there, this is Batool."
    assert actual == expected

def test_read_with_placeholders():
    actual = read_template("assets/test_with_placeholders.txt")
    expected = "Hello there, this is {Name}, I am {Age} years old."
    assert actual == expected

"""
**parse** test cases:
1. "" -> "", []
2. "Hello there, this is Batool" -> "Hello there, this is Batool", []
3. "Hello there, this is {Name}, I am {Age} years old." -> "Hello there, this is $, I am $ years old.", ["Name", "Age"]
"""
def test_parse_empty():
    actual1, actual2 = parse("")
    expected1, expected2 = "", []
    assert actual1 == expected1 and actual2 == expected2

def test_parse_no_placeholders():
    actual1, actual2 = parse("Hello there, this is Batool")
    expected1, expected2 = "Hello there, this is Batool", []
    assert actual1 == expected1 and actual2 == expected2

def test_parse_with_placeholders():
    actual1, actual2 = parse("Hello there, this is {Name}, I am {Age} years old.")
    expected1, expected2 = "Hello there, this is $, I am $ years old.", ["Name", "Age"]
    assert actual1 == expected1 and actual2 == expected2

"""
**merge** test cases:
1. "Hello there, this is Batool" , [] -> "Hello there, this is Batool"
3. "Hello there, this is $, I am $ years old", ["Batool", "24"] -> "Hello there, this is Batool, I am 24 years old"
"""

def test_merge_no_placeholders():
    actual = merge("Hello there, this is Batool", [])
    expected = "Hello there, this is Batool"
    assert actual == expected

def test_merge_with_placeholders():
    actual = merge("Hello there, this is $, I am $ years old", ["Batool", "24"])
    expected = "Hello there, this is Batool, I am 24 years old"
    assert actual == expected 