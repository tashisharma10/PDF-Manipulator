# All Rights Reserved.
# Copyright 2024 [Tashi Sharma]
# Unauthorized copying, modification, distribution, or any other use of this code is strictly prohibited.
import pikepdf
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

# Function to rotate PDF pages
def rotate_pdf(input_path, output_path):
    # Open the PDF file
    with pikepdf.Pdf.open(input_path) as pdf:
        # Rotate each page
        for page in pdf.pages:
            page.Rotate = 180
        # Save the modified PDF
        pdf.save(output_path)

# Create a Tkinter root window (it will not be shown)
Tk().withdraw() 

# Open file dialog for selecting a PDF file
input_file = askopenfilename(
  title="Select a PDF file",
   filetypes=[("PDF files", "*.pdf")]
)

# Check if a file was selected
if input_file:
    # Define the output file path
    output_file = os.path.splitext(input_file)[0] + "_rotated.pdf"
    
    # Rotate the PDF pages
    rotate_pdf(input_file, output_file)
    
    print(f"PDF rotated and saved as: {output_file}")
else:
    print("No file selected.")