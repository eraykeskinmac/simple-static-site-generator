def extract_title(markdown):
    """
    Extract the title from a markdown file.
    The title should be the first h1 header (line starting with a single #).
    """
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("# ").strip()
    raise ValueError("No h1 header found in markdown") 