# All Rights Reserved.
# Copyright 2024 [Tashi Sharma]
# Unauthorized copying, modification, distribution, or any other use of this code is strictly prohibited.
import tkinter as tk
from tkinter import filedialog
from pdf2image import convert_from_path
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
        # Convert PDF to images
        old_pdf = convert_from_path(pdf_path, poppler_path=r"C:\Users\ASHUTOSH KUMAR\Downloads\Release-24.07.0-0\poppler-24.07.0\Library\bin")
        
        # Use the directory of the selected PDF for saving images
        directory = os.path.dirname(pdf_path)
        
        # Save each page as an image
        for i, page in enumerate(old_pdf):
            image_path = os.path.join(directory, f"page_{i + 1}.png")
            page.save(image_path, "PNG")
            print(f"Page {i + 1} saved as '{image_path}'")

    except Exception as e:
        print(f"An error occurred: {e}")
