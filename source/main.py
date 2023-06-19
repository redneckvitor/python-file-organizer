import os
import hashlib
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

output_message = ''

image_extensions = [".png", ".jpg", ".jpeg", ".tif", ".tga", ".webp", ".PNG", ".JPG"]
video_extensions = [".mkv", ".mov", ".mp4", ".webm", ".MP4", ".MOV"]
compressed_extensions = [".zip", ".7z", ".rar"]
document_extensions = [".pdf", ".epub", ".txt", ".html", ".docx", ".csv", ".psd", ".json"]

def organize_files(path, type='images', extension_list=image_extensions):
    global output_message
    os.makedirs(f'{path}/{type}', exist_ok=True)

    for file_name in os.listdir(path):

        if any(file_name.endswith(extension) for extension in extension_list):

            file_path = os.path.join(path, file_name)

            output_message += f"\n{file_name}"

            try:
                shutil.move(file_path, f'{path}/{type}')
            except shutil.Error:
                print(f"{file_name} um arquivo de mesmo nome já existe na pasta")

def select_folder():
    folder = filedialog.askdirectory()
    return folder

def start_organizing():
    global output_message
    output_message = ''
    folder = select_folder()
    organize_files(folder, 'images', image_extensions)
    organize_files(folder, 'videos', video_extensions)
    organize_files(folder, 'compressed', compressed_extensions)
    organize_files(folder, 'documents', document_extensions)
    Path("output_log.txt").write_text(output_message)

root = tk.Tk()
root.geometry('800x600')

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

button = tk.Button(frame,
                   text="Organize",
                   command=start_organizing)
button.pack(side=tk.LEFT)

# Checkbox para ativar/desativar a remoção de duplicatas
remove_duplicates_var = tk.IntVar()
remove_duplicates_checkbox = tk.Checkbutton(frame, text="Remover duplicatas?", variable=remove_duplicates_var)
remove_duplicates_checkbox.pack(side=tk.RIGHT)

root.mainloop()
