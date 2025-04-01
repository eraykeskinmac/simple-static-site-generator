import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_to_html_with_props(self):
        node = ParentNode(
            "div",
            [LeafNode("span", "child")],
            {"class": "container", "id": "main"}
        )
        self.assertEqual(
            node.to_html(),
            '<div class="container" id="main"><span>child</span></div>'
        )

    def test_to_html_without_tag(self):
        node = ParentNode(None, [LeafNode("span", "child")])
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertEqual(str(cm.exception), "ParentNode requires a tag")

    def test_to_html_without_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertEqual(str(cm.exception), "ParentNode requires children")

    def test_to_html_with_empty_children(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_to_html_with_nested_parent_nodes(self):
        inner_node = ParentNode(
            "span",
            [LeafNode("b", "bold"), LeafNode("i", "italic")]
        )
        outer_node = ParentNode("div", [inner_node])
        self.assertEqual(
            outer_node.to_html(),
            "<div><span><b>bold</b><i>italic</i></span></div>"
        )

if __name__ == "__main__":
    unittest.main() 