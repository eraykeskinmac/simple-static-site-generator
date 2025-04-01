import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            tag="a",
            value="Click me",
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p", value="Hello")
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode(
            tag="div",
            value="Hello World",
            props={"class": "container"}
        )
        expected = 'HTMLNode(tag=div, value=Hello World, children=None, props={"class": "container"})'
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main() 