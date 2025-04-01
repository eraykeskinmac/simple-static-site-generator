from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not delimiter:
        return old_nodes
        
    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        splits = old_node.text.split(delimiter)
        
        if len(splits) % 2 == 0:
            raise ValueError(f"Invalid markdown syntax: unmatched delimiter {delimiter}")
            
        for i in range(len(splits)):
            if splits[i] == "":
                continue
                
            if i % 2 == 0:
                new_nodes.append(TextNode(splits[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(splits[i], text_type))
                
    return new_nodes 