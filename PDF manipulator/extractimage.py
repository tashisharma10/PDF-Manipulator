# All Rights Reserved.
# Copyright 2024 [Tashi Sharma]
# Unauthorized copying, modification, distribution, or any other use of this code is strictly prohibited.
import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF
from PIL import Image
import io
import os

# Function to open the file dialog and return the selected file path
def select_pdf():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")],
        title="Select a PDF file"
    )
    return file_path

# Get the selected PDF file from the file dialog
pdf_path = select_pdf()

# Check if a file was selected
if not pdf_path:
    print("No file selected.")
else:
    try:
        # Open the PDF using PyMuPDF
        pdf_document = fitz.open(pdf_path)
        
        # Use the directory of the selected PDF for saving images
        directory = os.path.dirname(pdf_path)
        
        # Iterate through pages of the PDF
        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)
            image_list = page.get_images(full=True)
            
            if not image_list:
                print(f"No images found on page {page_number + 1}.")
            else:
                for image_index, image in enumerate(image_list):
                    # Extract image bytes
                    xref = image[0]
                    base_image = pdf_document.extract_image(xref)
                    image_bytes = base_image["image"]
                    
                    # Convert image bytes to Pillow Image
                    pil_image = Image.open(io.BytesIO(image_bytes))
                    
                    # Define the output file path for the extracted image
                    output_file_path = os.path.join(directory, f"page_{page_number + 1}_image_{image_index + 1}.png")
                    
                    # Save the image data to a file
                    pil_image.save(output_file_path)
                    print(f"Extracted image saved as '{output_file_path}'")

    except Exception as e:
        print(f"An error occurred: {e}")