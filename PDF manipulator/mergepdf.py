# All Rights Reserved.
# Copyright 2024 [Tashi Sharma]
# Unauthorized copying, modification, distribution, or any other use of this code is strictly prohibited.
import tkinter as tk
from tkinter import filedialog
from pikepdf import Pdf
import os

# Function to open the file dialog and return the selected file paths
def select_pdfs():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_paths = filedialog.askopenfilenames(
        filetypes=[("PDF files", "*.pdf")],
        title="Select PDF files to merge"
    )
    return file_paths

# Get the selected PDF files from the file dialog
pdf_files = select_pdfs()

# Check if any files were selected
if not pdf_files:
    print("No files selected.")
else:
    try:
        # Create a new PDF to merge all selected PDFs into
        new_pdf = Pdf.new()
        
        # Use the directory of the first selected file for saving the merged PDF
        directory = os.path.dirname(pdf_files[0])
        
        # Iterate over the selected PDF files and merge them
        for file in pdf_files:
            old_pdf = Pdf.open(file)
            new_pdf.pages.extend(old_pdf.pages)
        
        # Define the output file path in the same directory as the first selected PDF
        output_file_path = os.path.join(directory, "merged_output.pdf")
        
        # Save the merged PDF to the defined output file path
        new_pdf.save(output_file_path)
        print(f"PDFs have been merged and saved as '{output_file_path}'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
