import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_empty(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_markdown_to_blocks_single_block(self):
        md = "This is a single paragraph with no breaks."
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a single paragraph with no breaks."])

    def test_markdown_to_blocks_multiple_breaks(self):
        md = """
First block

Second block


Third block
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First block",
                "Second block",
                "Third block",
            ],
        )

    def test_markdown_to_blocks_with_whitespace(self):
        md = """
    First block with leading whitespace

Second block with trailing whitespace    

Third block with both leading and trailing whitespace    
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First block with leading whitespace",
                "Second block with trailing whitespace",
                "Third block with both leading and trailing whitespace",
            ],
        )

    def test_markdown_to_blocks_with_heading(self):
        md = """
# Heading 1

## Heading 2

### Heading 3
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading 1",
                "## Heading 2",
                "### Heading 3",
            ],
        )

    def test_markdown_to_blocks_with_mixed_content(self):
        md = """
# Main Heading

This is a paragraph with **bold** and _italic_ text.

- List item 1
- List item 2
- List item 3

> This is a blockquote
> With multiple lines

`code block`
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Main Heading",
                "This is a paragraph with **bold** and _italic_ text.",
                "- List item 1\n- List item 2\n- List item 3",
                "> This is a blockquote\n> With multiple lines",
                "`code block`",
            ],
        ) 