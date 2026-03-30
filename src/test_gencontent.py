import pytest
from gencontent import extract_title

def test_extract_title():
    markdown = """# My Title
This is a paragraph.
"""
    expected = "My Title"
    actual = extract_title(markdown)
    assert actual == expected

def test_extract_title_no_h1():
    markdown = """## My Title
This is a paragraph.
"""
    with pytest.raises(Exception):
        extract_title(markdown)