def markdown_to_blocks(markdown):
    texts = markdown.strip().split("\n\n")
    new_texts = []
    for line in texts:
        new_texts.append(line.strip('\n'))
    return new_texts
if __name__ == "__main__":
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    blocks = markdown_to_blocks(md)
    print(blocks)
    