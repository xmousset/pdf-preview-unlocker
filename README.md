# PDF Preview Unlocker

A simple Python GUI application to unlock the preview of downloads PDFs files using Tkinter.\
The app provides two main options:

- **Select Files** : Opens a dialog to pick multiple PDF files to unlock.
- **Select Folder** : Opens a dialog to pick a folder; all PDFs in that folder will be unlocked.

## Code Structure
- `select_files()` : Lets the user select multiple PDF files and merges them.
- `select_folder()` : Lets the user select a folder and merges all PDFs inside.
- `merge_pdf(pdf_paths)` : Merges the given list of PDF files and prompts for the output location.
- `main_tk()` : Sets up the GUI and handles user interaction.
