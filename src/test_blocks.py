import unittest

from split_blocks import markdown_to_blocks
from blocks import BlockType, block_to_block_type
class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_type_heading(self):
        md = "### This is a line of text."
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)
    
    def test_type_heading_incorrect(self):
        md = "####### This is a line of text."
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_type_heading_incorrect_2(self):
        md = "#This is a line of text."
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_type_code(self):
        md = "``` This is a line of text. ```"
        self.assertEqual(block_to_block_type(md), BlockType.CODE)

    def test_type_code_incorrect(self):
        md = "``This is a line of text.```"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_type_quote(self):
        md = """
> This is a line of text.
> 4chan ahh text
>whoops no space
"""
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)

    def test_type_quote_incorrect(self):
        md = """
> This is a line of text.
> 4chan ahh text
whoops no >
"""
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_type_unordered(self):
        md = """
- one
- two
- three!
"""
        self.assertEqual(block_to_block_type(md), BlockType.UNORDERED_LIST)

    def test_type_unordered_incorrect(self):
        md = """
- one
- two
-three?
"""
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_type_ordered(self):
        md = """
1. one
2. two
3. three!
"""
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)

    def test_type_ordered_wrong(self):
        md = """
1. one
2. two
4. four?
"""
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)


    def test_type_paragraph(self):
        md = "Line of text!"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)
    


    