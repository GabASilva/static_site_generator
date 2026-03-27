from textnode import TextNode, TextType, text_node_to_html_node
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	
	for old_node in old_nodes:
		splitted_node = []
		if old_node.text_type != TextType.TEXT:
			new_nodes.append(old_node)
			continue
		sections = old_node.text.split(delimiter)
		if len(sections) % 2 == 0:
			raise Exception(f'Delimiter{delimiter} not closed')
		for i in range(0,len(sections)):
			if sections[i] == "":
				continue
			if i % 2 == 0:
				plain_text = TextNode(sections[i], TextType.TEXT)
				splitted_node.append(plain_text)
			else:
				special_type = TextNode(sections[i],text_type)
				splitted_node.append(special_type)
		new_nodes.extend(splitted_node)
	return new_nodes

def extract_markdown_images(text):
	pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
	return re.findall(pattern, text)

def extract_markdown_links(text):
	pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
	return re.findall(pattern, text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
	result = text
	result = split_nodes_delimiter([TextNode(result, TextType.TEXT)], "**", TextType.BOLD)
	result = split_nodes_delimiter(result, "_", TextType.ITALIC)
	result = split_nodes_delimiter(result, "`", TextType.CODE)
	result = split_nodes_image(result)
	result = split_nodes_link(result)
	return result