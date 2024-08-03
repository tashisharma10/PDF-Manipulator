# All Rights Reserved.
# Copyright 2024 [Tashi Sharma]
# Unauthorized copying, modification, distribution, or any other use of this code is strictly prohibited.
import tkinter as tk
from tkinter import filedialog
from pikepdf import Pdf, Page, Rectangle
import os

# Function to open the file dialog and return the selected file path
def select_pdf(title):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")],
        title=title
    )
    return file_path

# Get the two PDF files from the user
pdf_path1 = select_pdf("Select the first PDF file (base PDF)")
pdf_path2 = select_pdf("Select the second PDF file (overlay PDF)")

# Check if both files were selected
if not pdf_path1 or not pdf_path2:
    print("Both PDF files must be selected.")
else:
    try:
        # Open the selected PDFs
        old_pdf1 = Pdf.open(pdf_path1)
        old_pdf2 = Pdf.open(pdf_path2)

        # Ensure both PDFs have at least one page
        if not old_pdf1.pages or not old_pdf2.pages:
            print("One or both PDFs are empty.")
        else:
            # Get the first page from each PDF
            des_page = old_pdf1.pages[0]
            sur_page = old_pdf2.pages[0]

            # Add overlay from the second PDF onto the first PDF
            des_page.add_overlay(sur_page, Rectangle(0, 0, 500, 500))

            # Define the output file path in the same directory as the first PDF
            output_directory = os.path.dirname(pdf_path1)
            output_filename = "new_pdf.pdf"
            output_path = os.path.join(output_directory, output_filename)

            # Save the result to a new PDF
            old_pdf1.save(output_path)
            print(f"Overlayed PDF saved as '{output_path}'")

    except Exception as e:
        print(f"An error occurred: {e}")
