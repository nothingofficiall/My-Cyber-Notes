import os

path = input("Enter The Path of the Image: ")
output = os.popen(f"xxd -l 8 {path}").read()[10:29]

magic = {
    "8950 4e47 0d0a 1a0a": ".png",
    "ffd8 ffe0": ".jpeg", "ffd8 ffe1": ".jpeg", "ffd8 ffe2": ".jpeg",
    "ffd8 ffe3": ".jpeg", "ffd8 ffe8": ".jpeg",
    "2550 4446": ".pdf",
    "3c73 7667": ".svg"
}

ext = magic.get(output, None)
print(f"\n This file is a {ext}\n Magic number is {output}" if ext else "\n Unknown file type")

file_extension = os.path.splitext(path)[1].lower()
print(f"\n The file extension is showing: {file_extension}")

print(" This file is safe, Magic number matches the extension" if ext == file_extension else " This file is not safe, Magic number does not match the extension")
