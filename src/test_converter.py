import unittest

from converter import markdown_to_html_node
from textnode import TextNode, TextType 

class TestConverter(unittest.TestCase):
    def test_markdown_to_html_node(self):
        markdown = """# Heading 1

## Heading 2

### Heading 3"""
        result = markdown_to_html_node(markdown)
        self.assertEqual(result.to_html(), """<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3></div>""")

    def test_markdown_to_html_node_with_paragraphs(self):
        markdown = """# Heading 1

This is a paragraph.

## Heading 2

This is another paragraph."""
        result = markdown_to_html_node(markdown)
        self.assertEqual(result.to_html(), """<div><h1>Heading 1</h1><p>This is a paragraph.</p><h2>Heading 2</h2><p>This is another paragraph.</p></div>""")