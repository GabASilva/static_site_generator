import unittest

from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType

class TestDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        nodes = [TextNode("This is a **bold** node", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" node", TextType.TEXT)
        ])

    def test_split_nodes_delimiter_multiple(self):
        nodes = [TextNode("This is a **bold** and __italic__ node", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "__", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" node", TextType.TEXT)
        ])

    def test_split_nodes_delimiter_unclosed(self):
        nodes = [TextNode("This is an **unclosed node", TextType.TEXT)]
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertRaises(Exception, split_nodes_delimiter, nodes, "**", TextType.BOLD)

    def test_code_delimiter(self):
        nodes = [TextNode("Use `print()` here", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("Use ", TextType.TEXT),
            TextNode("print()", TextType.CODE),
            TextNode(" here", TextType.TEXT),
        ])

    def test_non_text_node_unchanged(self):
        nodes = [TextNode("already bold", TextType.BOLD)]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes, nodes)

    def test_bold_delimiter(self):
        nodes = [TextNode("a **bold** word", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ])

    def test_extract_markdown_images(self):
        text = "Here is an image: ![alt text](image.jpg)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("alt text", "image.jpg")])

    def test_extract_markdown_links(self):
        text = "Here is a link: [Google](https://google.com)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("Google", "https://google.com")])

    def test_extract_markdown_links_no_image(self):
        text = "Here is a link: [Google](https://google.com) and an image ![alt text](image.jpg)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("Google", "https://google.com")])

    def test_extract_markdown_links_no_link(self):
        text = "Here is an image ![alt text](image.jpg)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [])

    def test_extract_markdown_images_no_image(self):
        text = "Here is a link: [Google](https://google.com)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [])

    def test_extract_markdown_images_multiple(self):
        text = "Image 1: ![alt1](image1.jpg) and Image 2: ![alt2](image2.png)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("alt1", "image1.jpg"), ("alt2", "image2.png")])

    def test_extract_markdown_links_multiple(self):
        text = "Link 1: [Google](https://google.com) and Link 2: [GitHub](https://github.com)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("Google", "https://google.com"), ("GitHub", "https://github.com")])

    def test_text_to_textnodes(self):
        text = "This is a **bold** and _italic_ text with a [link](https://example.com) and an image ![alt](image.jpg)"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and an image ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "image.jpg"),
        ]
        self.assertEqual(nodes, expected_nodes)