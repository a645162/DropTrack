import os
import glob
import shutil

def remove_pycache(directory):
    # Use glob to find all __pycache__ directories
    pycache_dirs = glob.glob(os.path.join(directory, '**', '__pycache__'), recursive=True)
    
    for pycache_dir in pycache_dirs:
        print(f"Removing {pycache_dir}")
        try:
            # Remove the entire directory tree
            os.rmdir(pycache_dir) if os.listdir(pycache_dir) == [] else shutil.rmtree(pycache_dir)
        except OSError as e:
            print(f"Error: {pycache_dir} : {e.strerror}")

if __name__ == "__main__":
    # Start from the current working directory
    current_directory = os.getcwd()
    remove_pycache(current_directory)
