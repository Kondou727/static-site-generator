from block_to_html import markdown_to_html_node
import os
from pathlib import Path
def extract_title(markdown):
    with open(markdown, "r") as file:
        for line in file:
            if line.startswith("# "):
                return line.lstrip("# ").strip()
        raise Exception("Header not found!")
            
def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        markdown = file.read()
    with open(template_path, "r") as file:
        template = file.read()
    html = markdown_to_html_node(markdown).to_html().replace("href=\"/", f"href=\"{basepath}").replace("src=\"/", f"src=\"{basepath}")
    title = extract_title(from_path)
    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, 'w') as file:
        file.write(full_html)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if os.path.isfile(dir_path_content):
        generate_page(dir_path_content, template_path, Path(dest_dir_path).with_suffix(".html"), basepath)
    else:
        for path in os.listdir(dir_path_content):
            generate_page_recursive(os.path.join(dir_path_content, path), template_path, os.path.join(dest_dir_path, path), basepath)

    