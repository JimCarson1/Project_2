import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath('..'))

from helper import unzip_gz, zip_gz

def main():
    # Link to the helper module
    unzip_gz()
    zip_gz()

if __name__ == "__main__":
    main()