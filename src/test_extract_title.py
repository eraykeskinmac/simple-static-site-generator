import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_simple(self):
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_extract_title_with_whitespace(self):
        markdown = "#  Hello  "
        self.assertEqual(extract_title(markdown), "Hello")

    def test_extract_title_with_content(self):
        markdown = """# My Title
Some content here
## Subtitle
More content"""
        self.assertEqual(extract_title(markdown), "My Title")

    def test_extract_title_not_first_line(self):
        markdown = """Some content
# My Title
More content"""
        self.assertEqual(extract_title(markdown), "My Title")

    def test_extract_title_no_title(self):
        markdown = """Some content
## Subtitle
More content"""
        with self.assertRaises(ValueError) as cm:
            extract_title(markdown)
        self.assertEqual(str(cm.exception), "No h1 header found in markdown")

    def test_extract_title_h2_not_title(self):
        markdown = """## Not a title
# This is the title
More content"""
        self.assertEqual(extract_title(markdown), "This is the title")

    def test_extract_title_empty(self):
        markdown = ""
        with self.assertRaises(ValueError) as cm:
            extract_title(markdown)
        self.assertEqual(str(cm.exception), "No h1 header found in markdown") 