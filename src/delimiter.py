from textnode import TextNode, TextType, text_node_to_html_node

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

