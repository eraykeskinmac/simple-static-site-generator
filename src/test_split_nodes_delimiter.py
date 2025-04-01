import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_bold(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded phrase", TextType.BOLD),
                TextNode(" in the middle", TextType.TEXT),
            ]
        )

    def test_split_italic(self):
        node = TextNode("This is text with an _italic phrase_ in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic phrase", TextType.ITALIC),
                TextNode(" in the middle", TextType.TEXT),
            ]
        )

    def test_split_code(self):
        node = TextNode("This is text with a `code block` in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" in the middle", TextType.TEXT),
            ]
        )

    def test_split_multiple_nodes(self):
        nodes = [
            TextNode("This is text with a **bolded phrase**", TextType.TEXT),
            TextNode("This is already bold", TextType.BOLD),
            TextNode("This has another **bolded phrase**", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded phrase", TextType.BOLD),
                TextNode("This is already bold", TextType.BOLD),
                TextNode("This has another ", TextType.TEXT),
                TextNode("bolded phrase", TextType.BOLD),
            ]
        )

    def test_split_empty_delimiter(self):
        node = TextNode("This is text with a **bolded phrase**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "", TextType.BOLD)
        self.assertEqual(new_nodes, [node])

    def test_split_no_delimiter(self):
        node = TextNode("This is text without any delimiters", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [node])

    def test_split_unmatched_delimiter(self):
        node = TextNode("This is text with an **unmatched delimiter", TextType.TEXT)
        with self.assertRaises(ValueError) as cm:
            split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(str(cm.exception), "Invalid markdown syntax: unmatched delimiter **")

    def test_split_empty_text(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [])

    def test_split_empty_sections(self):
        node = TextNode("This is text with **bolded** and **more bolded** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("more bolded", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ]
        )

if __name__ == "__main__":
    unittest.main() 