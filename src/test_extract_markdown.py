import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            matches,
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )

    def test_extract_markdown_images_no_match(self):
        matches = extract_markdown_images("This is text with no images")
        self.assertListEqual([], matches)

    def test_extract_markdown_images_invalid_syntax(self):
        matches = extract_markdown_images("This is text with ![invalid syntax")
        self.assertListEqual([], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.boot.dev)"
        )
        self.assertListEqual([("link", "https://www.boot.dev")], matches)

    def test_extract_markdown_links_multiple(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            matches,
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
        )

    def test_extract_markdown_links_no_match(self):
        matches = extract_markdown_links("This is text with no links")
        self.assertListEqual([], matches)

    def test_extract_markdown_links_invalid_syntax(self):
        matches = extract_markdown_links("This is text with [invalid syntax")
        self.assertListEqual([], matches)

    def test_extract_markdown_links_and_images(self):
        text = "This is text with a [link](https://www.boot.dev) and an ![image](https://i.imgur.com/zjjcJKZ.png)"
        link_matches = extract_markdown_links(text)
        image_matches = extract_markdown_images(text)
        self.assertListEqual(
            link_matches,
            [("link", "https://www.boot.dev")],
        )
        self.assertListEqual(
            image_matches,
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
        )

    def test_extract_markdown_links_with_special_chars(self):
        text = "This is text with a [link with spaces](https://www.boot.dev/path with spaces)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            matches,
            [("link with spaces", "https://www.boot.dev/path with spaces")],
        )

if __name__ == "__main__":
    unittest.main() 