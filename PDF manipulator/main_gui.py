# All Rights Reserved.
# Copyright 2024 [Tashi Sharma]
# Unauthorized copying, modification, distribution, or any other use of this code is strictly prohibited.
import tkinter as tk
from tkinter import messagebox
import subprocess

class PDFManipulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Manipulator")
        self.file_path = None  # Initialize the file_path attribute

        tk.Label(root, text="Choose a PDF manipulation option:", padx=20, pady=20).grid(row=0, column=0, columnspan=3)

        buttons = [
            ("Rotate PDF", self.rotate_pdf),
            ("Reverse PDF", self.reverse_pdf),
            ("Encrypt PDF", self.encrypt_pdf),
            ("Extract Image from PDF", self.extract_image_pdf),
            ("Merge PDF", self.merge_pdf),
            ("Delete pages from PDF", self.delete_pages_from_pdf),
            ("Split PDF", self.split_pdf),
            ("PDF to Image", self.pdf2img_pdf),
            ("Reorder PDF", self.reorder_pdf),
            ("PDF to Docx", self.pdf_to_docx),
            ("Docx to PDF", self.docx_to_pdf),
            ("Watermark PDF", self.watermark_pdf),
        ]

        for i, (text, command) in enumerate(buttons):
            row = (i // 3) + 1
            column = i % 3
            button = tk.Button(root, text=text, command=command, padx=20, pady=10)
            button.grid(row=row, column=column, padx=5, pady=5, sticky='ew')
            button.bind("<Enter>", self.on_enter)
            button.bind("<Leave>", self.on_leave)

        for col in range(3):
            root.grid_columnconfigure(col, weight=1)

    def on_enter(self, event):
        event.widget.config(bg='lightblue')

    def on_leave(self, event):
        event.widget.config(bg='SystemButtonFace')

    def run_script(self, script_name):
        try:
            print(f"Running script: {script_name}")  # Debugging statement
            result = subprocess.run(['python', script_name], capture_output=True, text=True)
            output = result.stdout
            error_output = result.stderr
            if result.returncode == 0:
                messagebox.showinfo("Success", f"Operation completed successfully.\n\n{output}")
            else:
                messagebox.showerror("Error", f"An error occurred: {output}\n\n{error_output}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    def rotate_pdf(self):
        self.run_script('rotatepdf.py')

    def reverse_pdf(self):
        self.run_script('reversepdf.py')

    def encrypt_pdf(self):
        self.run_script('encryptpdf.py')

    def extract_image_pdf(self):
        self.run_script('extractimage.py')

    def merge_pdf(self):
        self.run_script('mergepdf.py')

    def split_pdf(self):
        self.run_script('splitpdf.py')

    def delete_pages_from_pdf(self):
        self.run_script('deletepage.py')

    def pdf2img_pdf(self):
        self.run_script('pdf2img.py')

    def watermark_pdf(self):
        self.run_script('watermark.py')

    def docx_to_pdf(self):
        self.run_script('convert_docx_to_pdf.py')

    def pdf_to_docx(self):
        self.run_script('convert_pdf_to_docx.py')

    def reorder_pdf(self):
        self.run_script('reorderpdf.py')

def create_gui():
    root = tk.Tk()
    app = PDFManipulatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    create_gui()
