import os
import shutil

downloads_folder = os.path.expanduser("~/Downloads")

image_extensions = [".png", ".jpg", ".jpeg", ".tif", ".tga", ".webp"]
video_extensions = [".mkv", ".mov", ".mp4", ".webm"]


def organize_files(path):
    """Recebe um diretório no parâmetro 'path' e organiza os arquivos"""

    os.makedirs(f'{path}/images', exist_ok=True)  # Cria uma nova pasta 'images' dentro do diretório escolhido
    os.makedirs(f'{path}/videos', exist_ok=True)  # Cria uma nova pasta 'videos' dentro do diretório escolhido


    for file_name in os.listdir(path):
        # Realiza uma operação para cada arquivo da pasta

        # Abaixo função para organizar os arquivos de imagem
        if any(file_name.endswith(extension) for extension in image_extensions):
            file_path = os.path.join(path, file_name)

            try:
                shutil.move(file_path, f'{path}/images')
            except shutil.Error:
                print(f"{file_name} um arquivo de mesmo nome já existe na pasta")

        # Abaixo função para organizar os arquivos de video
        if any(file_name.endswith(extension) for extension in video_extensions):
            file_path = os.path.join(path, file_name)

            try:
                shutil.move(file_path, f'{path}/videos')
            except shutil.Error:
                print(f"{file_name} um arquivo de mesmo nome já existe na pasta")



        print(file_name)  # debug


organize_files(downloads_folder) # Coloque aqui o caminho do diretório que você quer organizar
