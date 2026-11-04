# 4. Read from a File

# 12. Open the file in read mode and use file.read() to read and display its content.

import os

def read_from_file(filename="assignment_output.txt"):
    """Opens the text file in read mode and displays its content using file.read()."""

    if os.path.exists(filename):
        with open(filename, "r") as file:
            file_contents = file.read()
            print(f"Contents of '{filename}':")
            print("-" * 30)
            print(file_contents, end="")
            print("-" * 30)
    else:
        print(f"Error: The file '{filename}' does not exist.")


# ==========================================
# Main Execution Block
# ==========================================
if __name__ == "__main__":

    # Test Task 4: Read from File
    read_from_file()

    print("\nAll tasks executed successfully!")