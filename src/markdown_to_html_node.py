from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType
from block_types import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Invalid text type: {text_node.text_type}")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    
    if block_type == BlockType.PARAGRAPH:
        # Replace newlines with spaces for paragraphs
        text = " ".join(block.split("\n"))
        return ParentNode("p", text_to_children(text))
    elif block_type == BlockType.HEADING:
        # Split into lines and process each heading separately
        lines = block.split("\n")
        nodes = []
        for line in lines:
            if line.strip():
                level = len(line.split()[0])  # Count number of # characters
                text = line.lstrip("# ").strip()
                nodes.append(ParentNode(f"h{level}", text_to_children(text)))
        # Return all heading nodes directly without wrapping in a div
        return nodes
    elif block_type == BlockType.CODE:
        # Remove the backticks and handle code block specially
        code_text = block.strip("`").strip()
        # Preserve newlines in code blocks
        return ParentNode("pre", [ParentNode("code", [LeafNode(None, code_text + "\n")])])
    elif block_type == BlockType.QUOTE:
        # Remove the > prefix from each line and join with spaces
        quote_text = " ".join(line[2:].strip() for line in block.split("\n"))
        return ParentNode("blockquote", text_to_children(quote_text))
    elif block_type == BlockType.UNORDERED_LIST:
        # Split into list items and process each
        items = [item[2:].strip() for item in block.split("\n")]  # Remove "- " prefix
        return ParentNode("ul", [ParentNode("li", text_to_children(item)) for item in items])
    elif block_type == BlockType.ORDERED_LIST:
        # Split into list items and process each
        items = [item.split(". ", 1)[1].strip() for item in block.split("\n")]  # Remove "1. " prefix
        return ParentNode("ol", [ParentNode("li", text_to_children(item)) for item in items])
    else:
        raise ValueError(f"Invalid block type: {block_type}")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        if block.strip():  # Only process non-empty blocks
            nodes = block_to_html_node(block)
            # Handle both single nodes and lists of nodes (for headings)
            if isinstance(nodes, list):
                html_nodes.extend(nodes)
            else:
                html_nodes.append(nodes)
    return ParentNode("div", html_nodes) 