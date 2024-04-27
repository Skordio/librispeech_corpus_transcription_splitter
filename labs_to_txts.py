import os

def change_extension(root_dir, old_ext=".lab", new_ext=".txt"):
    # Traverse the directory tree
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            # Check if the file has the old extension
            if filename.endswith(old_ext):
                # Formulate the full path of the old file
                old_file = os.path.join(dirpath, filename)
                # Create new file name with new extension
                new_file = os.path.join(dirpath, filename[:-len(old_ext)] + new_ext)
                # Rename the file
                os.rename(old_file, new_file)
                print(f"Renamed '{old_file}' to '{new_file}'")

# Example usage:
# root_directory = "/path/to/your/directory"
# change_extension(root_directory)

if __name__ == "__main__":
    root_directory = input("Enter the path to the root directory: ")
    change_extension(root_directory)
