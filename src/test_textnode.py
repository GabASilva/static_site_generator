import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)

	def test_neq(self):
		node = TextNode("This is a text node", TextType.ITALIC)
		node2 = TextNode("This is also a text node",TextType.ITALIC)
		self.assertNotEqual(node,node2)

	def test_eq2(self):
		node = TextNode("This is a text node", TextType.BOLD, "www.google.com")
		node2 = TextNode("This is a text node", TextType.BOLD, "www.google.com")
		self.assertEqual(node, node2)

	def test_neq2(self):
		node = TextNode("This is a text node", TextType.BOLD,"www.uol.com.br")
		node2 = TextNode("This is a text node", TextType.BOLD,"www.casasbahia.com.br")
		self.assertNotEqual(node, node2)

	def test_totext(self):
		node = TextNode("This is a text node", TextType.TEXT)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")

	def test_tobold(self):
		node = TextNode("This is a bold node", TextType.BOLD)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "b")
		self.assertEqual(html_node.value, "This is a bold node")

	def test_toitalic(self):
		node = TextNode("This is an italic node", TextType.ITALIC)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "i")
		self.assertEqual(html_node.value, "This is an italic node")

	def test_tocode(self):
		node = TextNode("This is a code node", TextType.CODE)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "code")
		self.assertEqual(html_node.value, "This is a code node")

	def test_tolink(self):
		node = TextNode("This is a link node", TextType.LINK, "www.google.com")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "a")
		self.assertEqual(html_node.value, "This is a link node")
		self.assertEqual(html_node.props, {"href": "www.google.com"})

	def test_toimage(self):
		node = TextNode("This is an image node", TextType.IMAGE, "www.google.com")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "img")
		self.assertEqual(html_node.value, "")
		self.assertEqual(html_node.props, {"src": "www.google.com","alt":"This is an image node"})

if __name__ == "__main__":

	unittest.main()
