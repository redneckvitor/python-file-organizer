import os
import hashlib
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
import subprocess

output_message = ''

image_extensions = [".png", ".jpg", ".jpeg", ".tif", ".tga", ".webp"]
video_extensions = [".mkv", ".mov", ".mp4", ".webm", ".MP4", ".MOV"]
compressed_extensions = [".zip", ".7z", ".rar"]
document_extensions = [".pdf", ".epub", ".txt", ".html", ".docx", ".csv", ".psd"]


def remove_duplicates(folder):
    print("Removing duplicates...")
    hash_dict = {}
    for file in os.listdir(folder):

        filepath = os.path.join(folder, file)

        # apenas processar arquivos (não diretórios)
        if os.path.isfile(filepath):
            # calcular o hash SHA1 do arquivo
            file_hash = hash_file(filepath)

            # adicionar o arquivo ao dicionário de hashes
            if file_hash not in hash_dict:
                hash_dict[file_hash] = []
            hash_dict[file_hash].append(filepath)

    # para cada lista de arquivos com o mesmo hash
    for _, files in hash_dict.items():
        if len(files) > 1:
            print(f"Found {len(files)} duplicate files:")
            # manter o primeiro arquivo, excluir todos os outros
            for filepath in files[1:]:
                print(f"Deleting file {filepath}")
                os.remove(filepath)


def hash_file(filepath):
    # calcular o hash SHA1 de um arquivo
    BLOCK_SIZE = 65536
    file_hash = hashlib.sha1()
    with open(filepath, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    return file_hash.hexdigest()


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
    if folder:  # checando se uma pasta foi selecionada
        status_label.config(text="Processing...")
        root.update()
        if remove_duplicates_var.get() == 1:
            remove_duplicates(folder)
        organize_files(folder, 'images', image_extensions)
        organize_files(folder, 'videos', video_extensions)
        organize_files(folder, 'compressed', compressed_extensions)
        organize_files(folder, 'documents', document_extensions)
        Path("output_log.txt").write_text(output_message)
        status_label.config(text="Completed")
        root.update()

def open_log():
    subprocess.run(['notepad.exe', 'output_log.txt'])

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
remove_duplicates_checkbox.pack(side=tk.LEFT)

# Botão para abrir o log
log_button = tk.Button(frame,
                       text="Files Moved",
                       command=open_log)
log_button.pack(side=tk.RIGHT)

status_label = tk.Label(root, text="Waiting...")
status_label.pack(side=tk.BOTTOM)

root.mainloop()
