import os

# variable for path is made here
path = input("Enter The Path of the Image: ")

# reads the output of the command 
# and variable is added 
output = os.popen(f"xxd -l 8 {path}").read()

# slicing of the output string to get hexadecimal signature or magic number 
string_slice = output[10:29]

print(" ")

# assigning values to file formats
a = ".png"
b = ".jpeg"
c = ".pdf"
d = ".svg"

# defined a external variable
ext = None

# here we have a switch statement to tell which type file is this 
def check_file(string_slice):
    global ext  # used global to modify the variable outside the func.
    match string_slice:
        case "8950 4e47 0d0a 1a0a":
            print(f" This file is a {a}\n Magic number is 8950 4e47 0d0a 1a0a")
            ext = a 
        case "ffd8 ffe0" | "ffd8 ffe1" | "ffd8 ffe2" | "ffd8 ffe3" | "ffd8 ffe8":
            print(f" This file is a {b}\n Magic number is one of these ffd8 ffe0 or ffd8 ffe1 or ffd8 ffe2 or ffd8 ffe3 or ffd8 ffe8")
            ext = b
        case "2550 4446":
            print(f" This file is a {c}\n Magic number is 2550 4446")
            ext = c
        case "3c73 7667":
            print(f" This file is a {d}\n Magic number is 3c73 7667")
            ext = d
        case _:
            print(" Unknown file type")

check_file(string_slice)

print(" ")

# here we sliced the file extension
file_extension = os.path.splitext(path)[1].lower()
print(f" The file extension is showing : {file_extension}")

# checking if file format told using Magic number matches file extension 
if ext is not None and ext == file_extension:
    print(" This file is safe, Magic number matches the extension")
else:
    print(" This file is not safe, Magic number does not match the extension")



