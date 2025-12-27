# PDF Preview Unlocker

A simple Python GUI application (using Tkinter) to unlock the preview of downloaded PDF files on Windows.

When a PDF is downloaded from the internet, Windows may block its preview for security reasons. Normally, you can unlock a file by right-clicking it, selecting "Properties," and checking the "Unblock" box at the bottom. This app streamlines the process, allowing you to unlock multiple PDFs at once.

The app provides two main options:

- **Select Files** : Opens a dialog to pick multiple PDF files to unlock.
- **Select Folder** : Opens a dialog to pick a folder; all PDFs in that folder will be unlocked.

## Code Structure
- `UNLOCK` : if True, unlock the selected PDF files; otherwise, re-lock them.
- `select_files()` : lets the user select multiple PDF files and merges them.
- `select_folder()` : lets the user select a folder and merges all PDFs inside.
- `merge_pdf(pdf_paths)` : merges the given list of PDF files and prompts for the output location.
- `main_tk()` : sets up the GUI and handles user interaction.
