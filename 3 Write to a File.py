# 3. Write to a File

# 11. Write a program to create a text file and write some content to it, using file functions like open() and write().

def write_to_file(filename="assignment_output.txt"):
    """Creates a text file and writes sample content into it using open() and write()."""
    content = (
        "Hello, DevOps World!\n"
        "This file was created using Python file handling.\n"
        "Assignment 2 - Python & Bash Tasks Completed Successfully.\n"
    )

    with open(filename, "w") as file:
        file.write(content)

    print(f"Successfully wrote content to '{filename}'.")

write_to_file()