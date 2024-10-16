# Images-to-PDF Converter

This Python script allows you to convert a collection of images (PNG and JPG) from a specified directory into a single PDF file. It automates the task of merging multiple images into a PDF, providing a simple and efficient way to handle image-to-PDF conversion.

## Features

- Supports both **PNG** and **JPG** image formats.
- Automatically processes all images in the given directory.
- Outputs a single PDF file with all images combined.

## Prerequisites

Ensure you have the following installed on your system:

1. **Python 3.x**:  
   You can download and install Python from the official [Python website](https://www.python.org/).

2. **Required Python Library**:  
   Install the `img2pdf` library, which handles the conversion of images to PDF. You can install it using `pip`:
   ```bash
   pip install img2pdf
   ```

## Usage

1. Clone or download this repository to your local machine.

2. Make sure you have a directory containing the images you want to convert.

3. Run the script with the following steps:

   - Define the directory containing your images and specify the output PDF file path in the script.
   - Run the script using Python:
     ```bash
     python convert_images_to_pdf.py
     ```

   The script will process all `.png` and `.jpg` files in the directory and generate a PDF file.

## Code Overview

1. **Importing Modules**:
   - `os`: For interacting with the file system and accessing image files.
   - `img2pdf`: For converting the images to PDF format.

2. **Key Variables**:
   - `directory`: Path to the folder containing image files.
   - `output_file`: Path where the resulting PDF will be saved.

3. **Image Selection**:
   - The script collects all image files (`.png` or `.jpg`) from the specified directory.

4. **PDF Creation**:
   - The images are converted to PDF using `img2pdf.convert()` and written to the specified output file.

## Example

If you have images stored in the directory `./images`, and want to create a PDF called `output.pdf`, you would edit the script as follows:

```python
directory = './images'
output_file = 'output.pdf'
```

Then, run the script to generate the PDF.
