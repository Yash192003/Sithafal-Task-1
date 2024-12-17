

import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import re

def extract_text_from_image_page(pdf_path, page_number):
    """
    Extract text from a page in the PDF that contains an image.
    Converts the page into an image and extracts text using Tesseract OCR.
    """
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_number - 1)  # Page numbers are 0-indexed
    pix = page.get_pixmap()  # Render the page as an image
    img = Image.open(io.BytesIO(pix.tobytes("png")))  # Convert pixmap to PNG format
    text = pytesseract.image_to_string(img)  # Extract text using Tesseract
    return text

def extract_text_from_page(pdf_path, page_number):
    """
    Extract text from a text-based page in the PDF.
    """
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_number - 1)  # Load the specified page
    text = page.get_text()  # Extract text
    return text

def extract_tabular_data(page_text):
    """
    Extract tabular data from a page's text content.
    Cleans and organizes the table data into rows and columns.
    """
    lines = page_text.split('\n')  # Split text into lines
    table = []

    for line in lines:
        line = line.strip()
        if not line:  # Skip empty lines
            continue
        
        # Split line by spaces or multiple spaces
        row = re.split(r'\s{2,}|\t', line)  # Handles multiple spaces or tabs as separators
        if len(row) > 1:  # Ensure it's a valid table row
            table.append(row)

    return table

# Path to the PDF file
pdf_path = "C:/Users/yasha/OneDrive/Desktop/Sithafal/tables-charts-and-graphs-with-examples-from.pdf"

# Extract text from page 2 (image-based page)
page_2_text = extract_text_from_image_page(pdf_path, 2)
print("Extracted Text from Page 2:")
print(page_2_text)

# Extract text from page 6 (text-based page)
page_6_text = extract_text_from_page(pdf_path, 6)
print("\nExtracted Text from Page 6:")
print(page_6_text)

# Extract tabular data from Page 6
tabular_data = extract_tabular_data(page_6_text)
print("\nTabular Data from Page 6:")
for row in tabular_data:
    print(row)




