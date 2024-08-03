# All Rights Reserved.
# Copyright 2024 [Tashi Sharma]
# Unauthorized copying, modification, distribution, or any other use of this code is strictly prohibited.
import pikepdf
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.simpledialog import askstring
from tkinter import messagebox
import os

def encrypt_pdf(input_path, output_path, user_password, owner_password):
    # Define permissions
    permissions = pikepdf.Permissions(extract=False)

    # Open the PDF file
    with pikepdf.Pdf.open(input_path) as pdf:
        # Save the PDF with encryption
        pdf.save(output_path, encryption=pikepdf.Encryption(
            user=user_password,
            owner=owner_password,
            allow=permissions
        ))

def get_password(prompt):
    while True:
        password = askstring("Password", prompt, show='*')
        if password and password.isdigit() and len(password) == 6:
            return password
        else:
            messagebox.showerror("Invalid Password", "Password must be exactly 6 digits long. Please try again.")

# Create a Tkinter root window (it will not be shown)
Tk().withdraw()

# Open file dialog for selecting a PDF file
input_file = askopenfilename(
    title="Select a PDF file",
    filetypes=[("PDF files", "*.pdf")]
)

# Check if a file was selected
if input_file:
    # Get user and owner passwords from user
    user_password = get_password("Enter user password (6 digits):")
    owner_password = get_password("Enter owner password (6 digits):")
    
    if user_password and owner_password:
        # Define the output file path
        output_file = os.path.splitext(input_file)[0] + "_encrypted.pdf"
        
        # Encrypt the PDF
        encrypt_pdf(input_file, output_file, user_password, owner_password)
        
        print(f"PDF encrypted and saved as: {output_file}")
    else:
        print("Passwords not provided.")
else:
    print("No file selected.")