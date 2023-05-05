import os
import shutil

downloads_folder = os.path.expanduser("~/Downloads")

image_extensions = [".png", ".jpg", ".jpeg", ".tif", ".tga", ".webp"]
video_extensions = [".mkv", ".mov", ".mp4", ".webm"]
compressed_extensions = [".zip", ".7z", ".rar"]
document_extensions = [".pdf", ".epub", ".txt", ".html", ".docx", ".csv", ".psd"]


def organize_files(path, type='images', extension_list=image_extensions):
    """Separa os arquivos de um diretório, criando novas pastas.
    'path' = o caminho do diretório a ser organizado
    'type' = nome da pasta que será criada e onde os arquivos serão movidos
    'extension_list' = lista das extensões de arquivos a serem separados
    """

    os.makedirs(f'{path}/{type}', exist_ok=True)

    for file_name in os.listdir(path):

        if any(file_name.endswith(extension) for extension in extension_list):
            file_path = os.path.join(path, file_name)

            try:
                shutil.move(file_path, f'{path}/{type}')
            except shutil.Error:
                print(f"{file_name} um arquivo de mesmo nome já existe na pasta")

        print(file_name)  # debug


organize_files('test_folder', 'images', image_extensions)
