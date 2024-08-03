# All Rights Reserved.
# Copyright 2024 [Tashi Sharma]
# Unauthorized copying, modification, distribution, or any other use of this code is strictly prohibited.
import tkinter as tk
from tkinter import filedialog
import pikepdf
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
        # Open the selected PDF
        old_pdf = pikepdf.Pdf.open(pdf_path)
        
        # Reverse the order of the pages
        old_pdf.pages.reverse()
        
        # Define the output file path with "_reversed" appended to the original filename
        directory = os.path.dirname(pdf_path)
        filename = os.path.basename(pdf_path)
        name, ext = os.path.splitext(filename)
        output_file_path = os.path.join(directory, f"{name}_reversed{ext}")
        
        # Save the reversed PDF
        old_pdf.save(output_file_path)
        print(f"Reversed PDF saved as '{output_file_path}'")

    except Exception as e:
        print(f"An error occurred: {e}")