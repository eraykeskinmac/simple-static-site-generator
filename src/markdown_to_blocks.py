def markdown_to_blocks(markdown):
    # Split by double newlines and strip whitespace
    blocks = [block.strip() for block in markdown.split("\n\n")]
    
    # Remove empty blocks
    blocks = [block for block in blocks if block != ""]
    
    return blocks 