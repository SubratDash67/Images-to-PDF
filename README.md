# Images-to-PDF

This Python script converts a collection of image files (PNG and JPG) located in a specified directory into a single PDF file. Below are the requirements and a brief description of what the code does:

### Requirements:
1. **Python**: Ensure you have Python installed on your system. You can download and install Python from the official website: https://www.python.org/. Make sure to install Python 3.x.

2. **img2pdf**: This script uses the `img2pdf` library to convert image files to PDF. You can install it via pip, the Python package manager. Open a command prompt or terminal and run the following command:
   ```
   pip install img2pdf
   ```

### Code Description:
- **`import os`**: This imports the `os` module, which provides functions for interacting with the operating system.

- **`import img2pdf`**: This imports the `img2pdf` module, which is used for converting image files to PDF format.

- **`directory`**: This variable stores the path to the directory containing the image files to be converted.

- **`output_file`**: This variable stores the path to the output PDF file that will be generated.

- **`image_files`**: This list comprehension iterates over the files in the specified directory (`directory`) and creates a list of file paths for files ending with `.png` or `.jpg`.

- **`with open(output_file, "wb") as file`**: This opens the output file in binary write mode (`"wb"`), allowing us to write binary data to it. The `with` statement ensures that the file is properly closed after the block of code is executed.

- **`file.write(img2pdf.convert(image_files))`**: This line writes the PDF data generated from the image files to the output file. The `img2pdf.convert()` function takes a list of image file paths as input and returns the corresponding PDF data, which is then written to the output file.
