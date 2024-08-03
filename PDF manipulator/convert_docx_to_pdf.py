# All Rights Reserved.
# Copyright 2024 [Tashi Sharma]
# Unauthorized copying, modification, distribution, or any other use of this code is strictly prohibited.
import tkinter as tk
from tkinter import filedialog
from docx2pdf import convert
import os

# Function to open the file dialog and return the selected file path
def select_docx():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        filetypes=[("DOCX files", "*.docx")],
        title="Select a DOCX file"
    )
    return file_path

# Get the selected DOCX file from the file dialog
docx_path = select_docx()

# Check if a file was selected
if not docx_path:
    print("No file selected.")
else:
    try:
        # Define the output PDF file path
        directory = os.path.dirname(docx_path)
        filename = os.path.basename(docx_path)
        name, _ = os.path.splitext(filename)
        pdf_path = os.path.join(directory, f"{name}.pdf")

        # Convert DOCX to PDF
        convert(docx_path, pdf_path)
        
        print(f"Converted PDF saved as '{pdf_path}'")

    except Exception as e:
        print(f"An error occurred: {e}")
