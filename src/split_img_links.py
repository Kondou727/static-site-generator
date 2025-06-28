from md_extraction import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        node_text = node.text
        images = extract_markdown_images(node_text)
        if images == [] or node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue 
        for pair in images:
            sections = node_text.split(f"![{pair[0]}]({pair[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(pair[0], TextType.IMAGE, pair[1]))
            node_text = sections[1]
        if node_text != "":    
            new_nodes.append(TextNode(node_text, TextType.TEXT)) 
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        node_text = node.text
        links = extract_markdown_links(node_text)
        if links == [] or node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue 
        for pair in links:
            sections = node_text.split(f"[{pair[0]}]({pair[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(pair[0], TextType.LINK, pair[1]))
            node_text = sections[1]
        if node_text != "":    
            new_nodes.append(TextNode(node_text, TextType.TEXT)) 
    return new_nodes

if __name__ == "__main__":
    node = TextNode(
        "![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    node2 = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node]) + split_nodes_link([node2])
    print(new_nodes)