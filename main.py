import os
import subprocess
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox

UNLOCK = True

def select_files():
    """Opens a file dialog for the user to select multiple PDF files to merge.
    If at least two files are selected, converts those file paths to Path
    objects and calls merge_pdf with the Path list.
    """
    pdf_files = filedialog.askopenfilenames(
        title= "PDF unlocker - from files",
        filetypes= [("PDF files", "*.pdf")],
        initialdir= Path(__file__).parent
    )
    
    if not pdf_files:
        return None
    
    pdf_paths = [Path(f) for f in pdf_files]
    pdf_paths.sort()
    unlock_pdf(pdf_paths)


def select_folder():
    """Opens a folder dialog for the user to select a folder containing PDF
    files. If the folder contains at least two PDF files, converts those file
    paths to Path objects and calls merge_pdf with the Path list.
    """
    folder = filedialog.askdirectory(
        title= "PDF unlocker - from folder",
        initialdir= Path(__file__).parent,
    )
    if not folder:
        return None
    
    pdf_names = [f
        for f in os.listdir(folder)
        if f.lower().endswith(".pdf")
    ]
    
    if not pdf_names:
        messagebox.showerror("Error", "No PDF in selected folder.")
        return None
    
    pdf_paths = [Path(folder) / f for f in pdf_names]
    pdf_paths.sort()
    unlock_pdf(pdf_paths)


def unlock_pdf(pdf_paths : list[Path]):
    """Merges multiple PDF files into a single PDF file. Prompts the user to
    select the output pdf path via a save file dialog.
    """
    root = tk.Tk()
    root.withdraw()
    
    print(f"Unlocking PDFs...")
    
    for pdf in pdf_paths:
        
        if UNLOCK:
            process = f"Unblock-File -Path '{pdf}'"
        else:
            process = f"Set-Content -Path '{pdf}:Zone.Identifier' -Value '[ZoneTransfer]`nZoneId=3'"
        
        subprocess.run([
            "powershell",
            "-Command",
            process
            ])
        
        print(f"{pdf.name} done.")
    
    print(f"Unlocked done for {len(pdf_paths)} PDFs.")


def main_tk():
    """Creates the main tkinter window with buttons to select files or folder
    for PDF merging.
    """
    root = tk.Tk()
    root.title("PDF Merger")
    window_width = 400
    window_height = 100
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    pos_x = int(screen_width / 4 - window_width / 2)
    pos_y = int(screen_height / 4 - window_height / 2)
    root.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")
    root.resizable(False, False)
    
    nb_cols = 5
    nb_rows = 4
    
    label = tk.Label(
        root,
        text= "Choose a merging option:",
        font= ("Calibri", 15)
    )
    label.grid(row= 0, column= 0, columnspan= nb_cols)

    btn_files = tk.Button(
        root,
        text="Select Files",
        command= select_files,
        font= ("Calibri", 15, "bold")
    )
    btn_files.grid(row=2, column=1)

    btn_folder = tk.Button(
        root,
        text="Select Folder",
        command=select_folder,
        font= ("Calibri", 15, "bold")
    )
    btn_folder.grid(row=2, column=3)

    for i in range(nb_rows):
        root.grid_rowconfigure(i, weight= 1)
    
    for i in range(nb_cols):
        root.grid_columnconfigure(i, weight= 1)
    
    root.mainloop()


if __name__ == "__main__":
    main_tk()