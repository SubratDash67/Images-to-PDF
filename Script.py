import os
import img2pdf

directory = r"" #add your path to the images
output_file = r"" #path-to-images\output.pdf

image_files = [
    os.path.join(directory, i)
    for i in os.listdir(directory)
    if i.endswith((".png", ".jpg"))
]

with open(output_file, "wb") as file:
    file.write(img2pdf.convert(image_files))
