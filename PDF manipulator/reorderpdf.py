# All Rights Reserved.
# Copyright 2024 [Tashi Sharma]
# Unauthorized copying, modification, distribution, or any other use of this code is strictly prohibited.
import tkinter as tk
from tkinter import filedialog, simpledialog
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

# Function to prompt user for pages to replace
def get_pages_to_replace():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    replace_from = simpledialog.askinteger("Input", "Enter page number to replace:")
    replace_with = simpledialog.askinteger("Input", "Enter page number to use as replacement:")
    return replace_from, replace_with

# Get the selected PDF file from the file dialog
pdf_path = select_pdf()

# Check if a file was selected
if not pdf_path:
    print("No file selected.")
else:
    try:
        # Open the selected PDF
        old_pdf = pikepdf.Pdf.open(pdf_path)
        
        # Get the pages to replace from the user
        replace_from, replace_with = get_pages_to_replace()
        
        if replace_from is None or replace_with is None:
            print("Invalid page numbers provided.")
        else:
            # Convert 1-based index to 0-based index
            replace_from -= 1
            replace_with -= 1
            
            # Check if page numbers are within range
            if 0 <= replace_from < len(old_pdf.pages) and 0 <= replace_with < len(old_pdf.pages):
                # Replace the page
                old_pdf.pages[replace_from] = old_pdf.pages[replace_with]
                
                # Define the output file path
                directory = os.path.dirname(pdf_path)
                filename = os.path.basename(pdf_path)
                name, ext = os.path.splitext(filename)
                output_file_path = os.path.join(directory, f"{name}_replaced{ext}")
                
                # Save the modified PDF
                old_pdf.save(output_file_path)
                print(f"Modified PDF saved as '{output_file_path}'")
            else:
                print("Page numbers are out of range.")
                
    except Exception as e:
        print(f"An error occurred: {e}")
