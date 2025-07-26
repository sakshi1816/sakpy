import math
radius =float(input("Enter the radius of the circle:"))
area = math.pi * radius ** 2

print(f"The area of the circle with radius {radius} is: {area}")
filename = input("Input the Filename: ")

# Split the name by the dot
extension = filename.split(".")[-1]
extension_map = {
    "py": "python",
    "txt": "text",
    "cpp": "C++",
    "jpg": "image",
    "html": "HTML",
    "csv": "CSV",
  
}

# Get file type from map, fallback to the extension itself
file_type = extension_map.get(extension, extension)
print(f"The extension of the file is: '{file_type}'")
