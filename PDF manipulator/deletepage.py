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

# Function to prompt user for pages to delete
def get_pages_to_delete():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    pages_input = simpledialog.askstring(
        "Input", 
        "Enter page numbers to delete (e.g., 1,3,5 or 2-4):"
    )
    return pages_input

# Get the selected PDF file from the file dialog
pdf_path = select_pdf()

# Check if a file was selected
if not pdf_path:
    print("No file selected.")
else:
    try:
        # Open the selected PDF
        old_pdf = pikepdf.Pdf.open(pdf_path)
        
        # Get the pages to delete from the user
        pages_input = get_pages_to_delete()
        
        if not pages_input:
            print("No pages specified for deletion.")
        else:
            # Parse the pages input
            pages_to_delete = set()
            for part in pages_input.split(','):
                if '-' in part:
                    start, end = map(int, part.split('-'))
                    pages_to_delete.update(range(start - 1, end))  # Convert to zero-based index
                else:
                    pages_to_delete.add(int(part) - 1)  # Convert to zero-based index
            
            # Delete the specified pages
            pages_to_delete = sorted(pages_to_delete, reverse=True)  # Sort in reverse order for safe deletion
            for page_number in pages_to_delete:
                if 0 <= page_number < len(old_pdf.pages):
                    del old_pdf.pages[page_number]
                else:
                    print(f"Page number {page_number + 1} is out of range.")
            
            # Define the output file path
            directory = os.path.dirname(pdf_path)
            filename = os.path.basename(pdf_path)
            name, ext = os.path.splitext(filename)
            output_file_path = os.path.join(directory, f"{name}_del_modified{ext}")
            
            # Save the modified PDF
            old_pdf.save(output_file_path)
            print(f"Modified PDF saved as '{output_file_path}'")

    except Exception as e:
        print(f"An error occurred: {e}")