import unittest

from htmlnode import HTMLNode


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
       

if __name__ == "__main__":
    unittest.main()