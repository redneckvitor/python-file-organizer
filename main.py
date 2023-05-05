import os
import shutil

downloads_folder = os.path.expanduser("~/Downloads")
images_folder = os.path.expanduser("~/Downloads/images")

os.makedirs(images_folder, exist_ok=True)


def organize_files(path):
    """Recebe uma diretório no parâmetro 'path' e organiza os arquivos"""

    for file_name in os.listdir(path):

        if file_name.endswith(".png") or file_name.endswith(".jpg"):
            file_path = os.path.join(downloads_folder, file_name)

            try:
                shutil.move(file_path, images_folder)
            except shutil.Error:
                print(f"{file_name} already exists in the destination folder")

        print(file_name)  # debug


organize_files(downloads_folder)
