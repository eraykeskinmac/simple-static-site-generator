import os
import shutil
import logging

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

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Copy static files to public
    copy_static_to_public("static", "public")
    
    # TODO: Add markdown to HTML conversion here

if __name__ == "__main__":
    main()