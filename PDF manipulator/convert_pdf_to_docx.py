# All Rights Reserved.
# Copyright 2024 [Tashi Sharma]
# Unauthorized copying, modification, distribution, or any other use of this code is strictly prohibited.
import tkinter as tk
from tkinter import filedialog
from pdf2docx import Converter
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
        # Define the output DOCX file path
        directory = os.path.dirname(pdf_path)
        filename = os.path.basename(pdf_path)
        name, _ = os.path.splitext(filename)
        docx_path = os.path.join(directory, f"{name}.docx")

        # Convert PDF to DOCX
        converter = Converter(pdf_path)
        converter.convert(docx_path)
        converter.close()
        
        print(f"Converted DOCX saved as '{docx_path}'")

    except Exception as e:
        print(f"An error occurred: {e}")
