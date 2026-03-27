import unittest

from block_markdowns import markdown_to_blocks, block_to_block_type,BlockType
from textnode import TextNode, TextType

class TestBlockDelimiter(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "This is a block of text.\n\nThis is another block of text.\n\nThis is yet another block of text."
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, [
            "This is a block of text.",
            "This is another block of text.",
            "This is yet another block of text."
        ])
    
    def test_markdown_to_blocks_with_empty_lines(self):
        markdown = "This is a block of text.\n\n\n\nThis is another block of text.\n\n\n\nThis is yet another block of text."
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, [
            "This is a block of text.",
            "This is another block of text.",
            "This is yet another block of text."
        ])

    def test_markdown_to_blocks_with_leading_and_trailing_newlines(self):
        markdown = "\n\nThis is a block of text.\n\nThis is another block of text.\n\nThis is yet another block of text.\n\n"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, [
            "This is a block of text.",
            "This is another block of text.",
            "This is yet another block of text."
        ])

    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("```code\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("> Quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- Unordered list item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. Ordered list item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("This is a paragraph."), BlockType.PARAGRAPH)