# PDF Merger App

The PDF Merger App is a GUI tool for merging multiple PDF files into a single PDF. It is built using Python, Tkinter for the GUI, and PyPDF2 for handling the PDF operations.

## Features
- Add multiple PDF files to a list.
- Rearrange and remove PDFs before merging.
- Set a custom output filename for the merged PDF.
- Merges PDFs into a single output file saved in your Downloads folder by default.
- Re-order pages

## Prerequisites
- Python 3.6 or higher
- The following Python packages:
  - `PyPDF2`
  - `tkinter`

## Installation

1. **Clone the Repository**
   ```bash
     git clone https://github.com/rbeastbrook/pdfMerger_GUI.git
     cd pdfMerger_GUI
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
4. **Set the output filename** or leave it as default.
5. **Click `Merge PDFs`** to create the merged PDF.

   The merged PDF will be saved in the **Downloads** folder by default, or in a location of your choice.
   
Feel free to contribute or reach out for any issues!
