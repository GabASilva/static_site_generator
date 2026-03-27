from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from block_markdowns import markdown_to_blocks, block_to_block_type, BlockType
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode

def markdown_to_html_node(markdown_text):
    blocks = markdown_to_blocks(markdown_text)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            level = len(block) - len(block.lstrip("#"))
            text = block[level + 1:]
            children.append(ParentNode(f"h{level}", text_to_children(text)))
        elif block_type == BlockType.CODE:
            code = block.split("\n")
            code = "\n".join(code[1:-1])
            convert = TextNode(code, TextType.TEXT)
            children.append(ParentNode("pre", [ParentNode("code", [text_node_to_html_node(convert)])]))
        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            new_lines = [line.lstrip(">").strip() for line in lines]
            quote = " ".join(new_lines)
            children.append(ParentNode("blockquote", text_to_children(quote)))
        elif block_type == BlockType.UNORDERED_LIST:
            items = block.split("\n")
            list_items = []
            for item in items:
                text = item[item.find("- ") + 2:].strip()
                list_items.append(ParentNode("li", text_to_children(text)))
            children.append(ParentNode("ul", list_items))
        elif block_type == BlockType.ORDERED_LIST:
            items = block.split("\n")
            list_items = []
            for item in items:
                text = item[item.find(". ") + 2:].strip()
                list_items.append(ParentNode("li", text_to_children(text)))
            children.append(ParentNode("ol", list_items))
        else:
            lines = block.split("\n")
            paragraph = " ".join(lines)
            children.append(ParentNode("p", text_to_children(paragraph)))
    return ParentNode("div", children)

def text_to_children(texts):
    nodes = text_to_textnodes(texts)
    converted = []
    for node in nodes:
        converted.append(text_node_to_html_node(node))
    return converted