import os
import shutil
from pathlib import Path

# Cria o arquivo de log de sapida se ele não existir e caso exista
# ele limpa o arquivo 
Path('output_log.txt').write_text('')

downloads_folder = os.path.expanduser("~/Downloads")

image_extensions = [".png", ".jpg", ".jpeg", ".tif", ".tga", ".webp"]
video_extensions = [".mkv", ".mov", ".mp4", ".webm", ".MP4"]
compressed_extensions = [".zip", ".7z", ".rar"]
document_extensions = [".pdf", ".epub", ".txt", ".html", ".docx", ".csv", ".psd"]


def organize_files(path, type='images', extension_list=image_extensions):
    """Separa os arquivos de um diretório, criando novas pastas.
    'path' = o caminho do diretório a ser organizado
    'type' = nome da pasta que será criada e onde os arquivos serão movidos
    'extension_list' = lista das extensões de arquivos a serem separados
    """

    os.makedirs(f'{path}/{type}', exist_ok=True)

    output_message = Path("output_log.txt").read_text()

    for file_name in os.listdir(path):

        if any(file_name.endswith(extension) for extension in extension_list):

            file_path = os.path.join(path, file_name)

            output_message += f"\n{file_name}"
            print(output_message)

            try:
                shutil.move(file_path, f'{path}/{type}')
            except shutil.Error:
                print(f"{file_name} um arquivo de mesmo nome já existe na pasta")

        Path("output_log.txt").write_text(output_message)
        #print(file_name)  # debug


organize_files('test_folder', 'images', image_extensions)
organize_files('test_folder', 'videos', video_extensions)
organize_files('test_folder', 'compressed', compressed_extensions)
organize_files('test_folder', 'documents', document_extensions)
