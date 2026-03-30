import os
import shutil
from converter import markdown_to_html_node

def extract_title(markdown):
	lines = markdown.split("\n")
	for line in lines:
		if line.startswith("# "):
			return line[2:].strip()
	raise Exception ("No h1 header found in markdown") 

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} using template {template_path} to {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()
    origin_converted = markdown_to_html_node(markdown_content).to_html()
    origin_title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", origin_title)
    template = template.replace("{{ Content }}", origin_converted)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    dest_file = open(dest_path, "w")
    dest_file.write(template)
    dest_file.close()

def generate_pages_recursive(source_dir_path, template_path, dest_dir_path):
    to_path = dest_dir_path
    from_path = source_dir_path
    for file in os.listdir(from_path):
        from_file_path = os.path.join(from_path, file)
        to_file_path = os.path.join(to_path, file)
        if os.path.isdir(from_file_path):
            if not os.path.exists(to_file_path):
                os.mkdir(to_file_path)
            generate_pages_recursive(from_file_path, template_path, to_file_path)
        else:
            to_file_path = to_file_path.replace(".md", ".html")
            generate_page(from_file_path, template_path, to_file_path)
