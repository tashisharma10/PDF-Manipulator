# All Rights Reserved.
# Copyright 2024 [Tashi Sharma]
# Unauthorized copying, modification, distribution, or any other use of this code is strictly prohibited.
import pikepdf
import tkinter as tk
from tkinter import filedialog
import os

# Function to open the file dialog and return the selected file path
def select_pdf_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")],
        title="Select a PDF file"
    )
    return file_path

# Get the PDF file path from the file dialog
pdf_path = select_pdf_file()

# Check if a file was selected
if not pdf_path:
    print("No file selected.")
else:
    try:
        # Extract the directory of the original PDF
        directory = os.path.dirname(pdf_path)
        old_pdf = pikepdf.Pdf.open(pdf_path)
        
        for n, page in enumerate(old_pdf.pages):
            new_pdf = pikepdf.Pdf.new()
            new_pdf.pages.append(page)
            name = os.path.join(directory, f"test{n}.pdf")
            new_pdf.save(name)
            print(f"Saved page {n+1} as {name}")

    except Exception as e:
        print(f"An error occurred: {e}")