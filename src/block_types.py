from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    # Check for headings (1-6 # characters followed by space)
    if block.startswith("#"):
        for i in range(1, 7):
            if block.startswith("#" * i + " "):
                return BlockType.HEADING
        return BlockType.PARAGRAPH
    
    # Check for code blocks (3 backticks at start and end)
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    # Check for quote blocks (any line starts with > and space)
    lines = block.split("\n")
    if any(line.startswith("> ") for line in lines):
        return BlockType.QUOTE
    
    # Check for unordered lists (every line starts with - and space)
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    # Check for ordered lists (every line starts with number. and space)
    if all(line.startswith(f"{i+1}. ") for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    
    # If none of the above, it's a paragraph
    return BlockType.PARAGRAPH 