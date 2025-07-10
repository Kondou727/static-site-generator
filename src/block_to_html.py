from split_blocks import markdown_to_blocks
from blocks import block_to_block_type, BlockType
from htmlnode import ParentNode, text_node_to_html_node
from text_to_textnode import text_to_textnodes
from textnode import TextNode, TextType
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        match (block_to_block_type(block)):
            case (BlockType.PARAGRAPH):
                node = ParentNode("p", text_to_children(block))
            case (BlockType.HEADING):
                node = ParentNode(f"h{len(block.split(" ", 1)[0])}", text_to_children(extract_heading(block)))
            case (BlockType.CODE):
                node = ParentNode("pre", [text_node_to_html_node(TextNode(extract_code(block).lstrip("\n"), TextType.CODE))])
            case (BlockType.ORDERED_LIST):
                split_list = block.split("\n")
                node_list = []
                for line in split_list:
                    node = ParentNode("li", text_to_children(extract_list(line)))
                    node_list.append(node)
                node = ParentNode("ol", node_list)
            case (BlockType.UNORDERED_LIST):
                split_list = block.split("\n")
                node_list = []
                for line in split_list:
                    node = ParentNode("li", text_to_children(extract_list(line)))
                    node_list.append(node)
                node = ParentNode("ul", node_list)
            case (BlockType.QUOTE):
                    node = ParentNode("blockquote", text_to_children(extract_quote(block)))
        nodes.append(node)
    return ParentNode("div", nodes)

                                
def extract_heading(block):
    return block.split(" ", 1)[1]
def extract_code(block):
    return block[3:-3]
def extract_list(line):
    return line.split(" ", 1)[1]
def extract_quote(block):
    split_lines = block.split("\n")
    temp = []
    for l in split_lines:
        temp.append(l.strip("> "))
    return " ".join(temp)
def text_to_children(text):
    new_text = text.replace("\n", " ")
    textnodes = text_to_textnodes(new_text)
    leafnodes = []
    for node in textnodes:
        leafnodes.append(text_node_to_html_node(node))
    return leafnodes