import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """
# Heading 1
## Heading 2
### Heading 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3></div>",
        )

    def test_heading_with_inline(self):
        md = """
# Heading with **bold** and _italic_
## Heading with `code` and [link](https://example.com)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading with <b>bold</b> and <i>italic</i></h1><h2>Heading with <code>code</code> and <a href=\"https://example.com\">link</a></h2></div>",
        )

    def test_quote(self):
        md = """
> This is a quote
> With multiple lines
> And **bold** text
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote With multiple lines And <b>bold</b> text</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- First item
- Second item with **bold**
- Third item with _italic_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>First item</li><li>Second item with <b>bold</b></li><li>Third item with <i>italic</i></li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. First item
2. Second item with `code`
3. Third item with [link](https://example.com)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item with <code>code</code></li><li>Third item with <a href=\"https://example.com\">link</a></li></ol></div>",
        )

    def test_mixed_blocks(self):
        md = """
# Main Heading

This is a paragraph with **bold** and _italic_.

> This is a quote block
> With multiple lines

- List item 1
- List item 2 with `code`

1. Ordered item 1
2. Ordered item 2 with [link](https://example.com)

```
This is a code block
That should not be parsed
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Main Heading</h1><p>This is a paragraph with <b>bold</b> and <i>italic</i>.</p><blockquote>This is a quote block With multiple lines</blockquote><ul><li>List item 1</li><li>List item 2 with <code>code</code></li></ul><ol><li>Ordered item 1</li><li>Ordered item 2 with <a href=\"https://example.com\">link</a></li></ol><pre><code>This is a code block\nThat should not be parsed\n</code></pre></div>",
        )

    def test_empty_markdown(self):
        md = ""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div></div>")

    def test_whitespace_only(self):
        md = "   \n  \n  "
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div></div>") 