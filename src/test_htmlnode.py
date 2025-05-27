import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        prop = {"href": "https://www.google.com","target": "_blank",}
        node = HTMLNode(value="Hello world!", props=prop)
        expected_result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_result)
    def test_props_to_html_2(self):
        prop = {}
        node = HTMLNode(value="Hello world!", props=prop)
        expected_result = ''
        self.assertEqual(node.props_to_html(), expected_result)
    def test_empty(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "HTMLNode(None, None, None, None)")
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()