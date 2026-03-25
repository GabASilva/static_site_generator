import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
	def test_eq(self):
        	node = TextNode("This is a text node", TextType.BOLD)
        	node2 = TextNode("This is a text node", TextType.BOLD)
        	self.assertEqual(node, node2)

	def test_neq(self):
		node = TextNode("This is a text node", TextType.ITALIC)
		node2 = TextNode("This is also a text node",TextType.ITALIC)
		self.asserNotEqual(node,node2)

	def test_eq2(self):
	        node = TextNode("This is a text node", TextType.BOLD, "www.google.com")
	        node2 = TextNode("This is a text node", TextType.BOLD, "www.google.com")
	        self.assertEqual(node, node2)

	def test_neq(self):
	        node = TextNode("This is a text node", TextType.BOLD,"www.uol.com.br")
	        node2 = TextNode("This is a text node", TextType.BOLD,"www.casasbahia.com.br")
	        self.assertNotEqual(node, node2)


if __name__ == "__main__":
	unittest.main()
