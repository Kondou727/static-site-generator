import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_type(self):
        node = TextNode("A", TextType.ITALIC)
        node2 = TextNode("A", TextType.NORMAL)
        self.assertNotEqual(node, node2)
    def test_text(self):
        node = TextNode("A", TextType.NORMAL)
        node2 = TextNode("B", TextType.NORMAL)
        self.assertNotEqual(node, node2)
    def test_url(self):
        node = TextNode("A", TextType.LINK)
        node2 = TextNode("A", TextType.LINK, None)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()