import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog, messagebox

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.pdf_files = []

        # Set the default output directory to the Downloads folder
        self.downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        self.default_output_filename = os.path.join(self.downloads_folder, "merged.pdf")

        # Create GUI elements
        self.label = tk.Label(root, text="Select PDF files to merge:")
        self.label.pack(pady=10)

        self.listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50, height=10)
        self.listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Add PDF", command=self.add_pdf)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Remove Selected", command=self.remove_pdf)
        self.remove_button.pack(pady=5)

        self.merge_button = tk.Button(root, text="Merge PDFs", command=self.merge_pdfs)
        self.merge_button.pack(pady=20)

        self.output_label = tk.Label(root, text="Output filename:")
        self.output_label.pack(pady=5)

        self.output_entry = tk.Entry(root, width=50)
        self.output_entry.insert(0, self.default_output_filename)  # Set default output filename
        self.output_entry.pack(pady=5)

    def add_pdf(self):
        file_paths = filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF Files", "*.pdf")])
        for file_path in file_paths:
            if file_path not in self.pdf_files:
                self.pdf_files.append(file_path)
                self.listbox.insert(tk.END, os.path.basename(file_path))

    def remove_pdf(self):
        selected_indices = self.listbox.curselection()
        for index in reversed(selected_indices):
            self.listbox.delete(index)
            del self.pdf_files[index]

    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showwarning("Warning", "No PDF files selected!")
            return
        
        output_filename = self.output_entry.get()
        if not output_filename.endswith('.pdf'):
            output_filename += '.pdf'

        merger = PyPDF2.PdfMerger()
        try:
            for pdf in self.pdf_files:
                merger.append(pdf)
                print(f"Merging {pdf}...")  # This can be removed for GUI-only feedback

            with open(output_filename, "wb") as output_file:
                merger.write(output_file)

            messagebox.showinfo("Success", f"Merged PDFs into {os.path.abspath(output_filename)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {e}")
        finally:
            merger.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
