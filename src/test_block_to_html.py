import unittest
from block_to_html import markdown_to_html_node
class TestBlock_to_HTML(unittest.TestCase):
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
        
    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )           

    def test_heading_with_inline(self):
        md = "# Welcome to the **Jungle**"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>Welcome to the <b>Jungle</b></h1></div>")
    
    def test_quote_block(self):
        md = "> This is a _quote_ block"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><blockquote>This is a <i>quote</i> block</blockquote></div>")

    def test_unordered_list(self):
        md = "- Item 1\n- Item **2**\n- Item _3_"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
           "<div><ul><li>Item 1</li><li>Item <b>2</b></li><li>Item <i>3</i></li></ul></div>")
        
    def test_mixed_content(self):
        md = (
            "# Header\n\n"
            "Paragraph with **bold** and _italic_.\n\n"
            "```\n"
            "Code block\n"
            "with line breaks\n"
            "```\n\n"
            "> Blockquote!"
        )
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Header</h1><p>Paragraph with <b>bold</b> and <i>italic</i>.</p>"
            "<pre><code>Code block\nwith line breaks\n</code></pre>"
            "<blockquote>Blockquote!</blockquote></div>"
        )