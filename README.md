# PDF Tool (GUI) - PDF Merger & to Word Converter

The PDF Merger & PDF to Word Converter is a user-friendly GUI tool that lets you **merge multiple PDF files** into a single PDF and **convert PDFs to Word (.docx) format**. It’s built using Python, Tkinter for the GUI, PyPDF2 for merging and reordering, and pdf2docx for PDF to Word conversion.

## Features
- Add multiple PDF files to a list.
- Rearrange and remove PDFs before merging.
- Set a custom output filename for the merged PDF.
- Merges PDFs into a single output file saved in your Downloads folder by default.
- Re-order pages within a PDF file.
- Convert PDF files to Word (.docx) format.

## Prerequisites
- Python 3.6 or higher
- The following Python packages:
  - `PyPDF2`
  - `tkinter`
  - `pdf2docx`

## Installation

1. **Clone the Repository**
   ```bash
     git clone https://github.com/rbeastbrook/pdftool.git
     cd pdftool
   ```
2. **Install Dependencies Make sure you have Python installed, then run:**
  ```bash
    pip install -r requirements.txt
  ```
3. **Run the Application To start the GUI application:**
```bash
  python pdfTool.py
```
## Usage

1. **Launch the application.**
2. **Click `Add PDF`** to select PDF files to be merged.
3. **Click `Remove Selected`** to remove any selected files from the list.
4. **Click `Reorder Pages` ** to change the page order within a PDF
5. **Click `Merge PDFs`** to create the merged PDF.
6. **Click `Convert to Word`** to convert selected PDFs to Word documents.
7. **Set the output filename** or leave it as default.
The merged PDF will be saved in the **Downloads** folder by default, or can be overwritten to  a location of your choice. The word document will bring up a save dialog box.

   
Feel free to contribute or reach out for any issues!
