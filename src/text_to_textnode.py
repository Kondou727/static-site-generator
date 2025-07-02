from split_img_links import split_nodes_image, split_nodes_link
from textnode import split_nodes_delimiter, TextType, TextNode

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    split_link = split_nodes_link(split_nodes_image([node]))
    split_images = split_nodes_image(split_link)
    split_italic = split_nodes_delimiter(split_images, "_", TextType.ITALIC)
    split_bold = split_nodes_delimiter(split_italic, "**", TextType.BOLD)
    split_code = split_nodes_delimiter(split_bold, "`", TextType.CODE)
    return split_code

if __name__ == "__main__":
    test_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    for node in text_to_textnodes(test_text):
        print(node)