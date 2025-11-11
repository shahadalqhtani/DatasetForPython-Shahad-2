import zipfile
import os

def unzip_archive(zip_path, extract_to):
    # Ensure the extraction directory exists
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def main():
    # Define the path to the ZIP file and the directory where it should be extracted
    zip_path = 'archive.zip'
    extract_dir = '/tmp/unpack'

    # Call the function to unzip the archive
    unzip_archive(zip_path, extract_dir)
    print(f"All files from {zip_path} have been extracted to {extract_dir}")

if __name__ == "__main__":
    main()