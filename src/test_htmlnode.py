import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
	def test_props_to_html_single(self):
		node = HTMLNode(props={"href": "https://google.com"})
		self.assertEqual(node.props_to_html(), ' href="https://google.com"')

	def test_props_to_html_multiple(self):
		node = HTMLNode(props={"href": "https://google.com", "tag": "head"})
		self.assertEqual(node.props_to_html(), ' href="https://google.com" tag="head"')

	def test_props_to_html_none(self):
		node = HTMLNode()
		self.assertEqual(node.props_to_html(), '')

	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_leaf_to_html_a(self):
		node = LeafNode("a", "Hello, Title",{"href": "https://google.com"})
		self.assertEqual(node.to_html(), '<a href="https://google.com">Hello, Title</a>')

	def test_leaf_to_html_none(self):
		node = LeafNode(None, "Hai, world!")
		self.assertEqual(node.to_html(), "Hai, world!")


	def test_leaf_to_html_error(self):
		node = LeafNode("p", None)
		with self.assertRaises(ValueError):
			node.to_html()

	def test_to_html_parent_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_parent_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
        		parent_node.to_html(),
        		"<div><span><b>grandchild</b></span></div>",
    		)

	def test_to_html_parent_notag(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode(None, [child_node])
		with self.assertRaises(ValueError):
			parent_node.to_html()

	def test_to_html_parent_multiplechild(self):
		child_node = LeafNode("span", "child")
		child_node2 = LeafNode("b", "child2")
		parent_node = ParentNode("div", [child_node, child_node2])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span>child</span><b>child2</b></div>",
		)
