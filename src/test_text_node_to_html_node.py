import unittest
from textnode import TextNode, TextType
from text_node_to_html_node import text_node_to_html_node

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")

    def test_italic(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text")

    def test_code(self):
        node = TextNode("This is code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code text")

    def test_link(self):
        node = TextNode("Click me", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_image(self):
        node = TextNode("Alt text", TextType.IMAGE, "https://example.com/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {
            "src": "https://example.com/image.jpg",
            "alt": "Alt text"
        })

    def test_link_without_url(self):
        node = TextNode("Click me", TextType.LINK)
        with self.assertRaises(ValueError) as cm:
            text_node_to_html_node(node)
        self.assertEqual(str(cm.exception), "Link TextNode must have a URL")

    def test_image_without_url(self):
        node = TextNode("Alt text", TextType.IMAGE)
        with self.assertRaises(ValueError) as cm:
            text_node_to_html_node(node)
        self.assertEqual(str(cm.exception), "Image TextNode must have a URL")

    def test_invalid_text_type(self):
        node = TextNode("Invalid type", "invalid_type")
        with self.assertRaises(ValueError) as cm:
            text_node_to_html_node(node)
        self.assertEqual(str(cm.exception), "Invalid text type: invalid_type")

    def test_invalid_input_type(self):
        with self.assertRaises(ValueError) as cm:
            text_node_to_html_node("not a TextNode")
        self.assertEqual(str(cm.exception), "Input must be a TextNode")

if __name__ == "__main__":
    unittest.main() 