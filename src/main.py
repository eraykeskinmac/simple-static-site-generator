import os
import shutil
import logging
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def copy_static_to_public(source_dir, dest_dir):
    """
    Recursively copy all contents from source_dir to dest_dir.
    First deletes all contents of dest_dir to ensure a clean copy.
    """
    # Delete the destination directory if it exists
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    
    # Create the destination directory
    os.makedirs(dest_dir)
    
    def copy_recursive(src, dst):
        # Get all items in the source directory
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            dst_path = os.path.join(dst, item)
            
            # Log the path being copied
            logging.info(f"Copying {src_path} to {dst_path}")
            
            if os.path.isfile(src_path):
                # If it's a file, copy it
                shutil.copy2(src_path, dst_path)
            else:
                # If it's a directory, create it and recurse
                os.makedirs(dst_path, exist_ok=True)
                copy_recursive(src_path, dst_path)
    
    # Start the recursive copy
    copy_recursive(source_dir, dest_dir)

def generate_page(from_path, template_path, dest_path):
    """
    Generate an HTML page from a markdown file using a template.
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read the markdown file
    with open(from_path, "r") as f:
        markdown = f.read()
    
    # Read the template file
    with open(template_path, "r") as f:
        template = f.read()
    
    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown)
    content = html_node.to_html()
    
    # Extract the title
    title = extract_title(markdown)
    
    # Replace placeholders in the template
    html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    
    # Create the destination directory if it doesn't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write the HTML file
    with open(dest_path, "w") as f:
        f.write(html)

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Copy static files to public
    copy_static_to_public("static", "public")
    
    # Generate the index page
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()