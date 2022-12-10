import os
from pathlib import Path
import sys, shutil

EXTENSIONS = {
    "images": ('.jpeg', '.png', '.jpg', '.svg'),
    "video": ('.avi', '.mp4', '.mov', '.mkv'),
    "documents": ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'),
    "audio": ('.mp3', '.ogg', '.wav', '.amr'),
    "archives": ('.zip', '.gz', '.tar')
}


def clean(folder: Path) -> None:
    for file in folder.iterdir():
        file = []
        if file.is_file():
            sort_files(file, folder)

            if file.endswith(EXTENSIONS['images']):
                shutil.move(os.path.join(folder), file_destination)
                print(f'Image moved to "images": {file}')
            elif file.endswith(EXTENSIONS['video']):
                shutil.move(os.path.join(folder), file_destination)
                print(f'Video moved to "videos":{file}')
            elif file.endswith(EXTENSIONS['documents']):
                shutil.move(os.path.join(folder), file_destination)
                print(f'Document moved to "documents":{file}')
            elif file.endswith(EXTENSIONS['audio']):
                shutil.move(os.path.join(folder), file_destination)
                print(f'Audio moved to "audio":{file}')
            elif file.endswith(EXTENSIONS['archives']):
                shutil.move(os.path.join(folder), file_destination)
                print(f'Archive moved to "archives":{file}')
            sort_files(file, folder)


        else:
            if file.name not in EXTENSIONS.keys():
                sub_folder = file
            if not os.listdir(sub_folder):
                shutil.rmtree(sub_folder)
                return
            clean(sub_folder)


def sort_files(file: Path, folder: Path):
    for folder_name, extensions in EXTENSIONS.items():
        if file.suffix in extensions:
            new_folder = folder.joinpath(folder_name)
            new_folder.mkdir(exist_ok=True)
            new_file_name = normalize(file.name.removesuffix(file.suffix))
            new_file = file.rename(new_folder.joinpath(new_file_name + file.suffix))

            if folder_name == 'archives':
                archive_unpack(new_folder, new_file)

            break

    else:
        new_file_name = normalize(file.name.removesuffix(file.suffix))

        file.rename(folder.joinpath(new_file_name + file.suffix))


def normalize(file_name):
    file.name = file.name.lower()
    new_file_name = normalize(file.name.removesuffix(file.suffix))
    file.rename(new_folder.joinpath(new_file_name + file.suffix))
    return file_name


def archive_unpack(folder: Path, file: Path):
    archive_folder = folder.joinpath(file.name.removesuffix(file.suffix))
    archive_folder.mkdir(exist_ok=True)
    shutil.unpack_archive(folder.joinpath(file), archive_folder)
    print("Archive file unpacked successfully.")


def main(Path):
    if len(sys.argv) < 2:
        print('Enter path to folder which should be cleaned: ')
        exit()

    root_folder = Path(sys.argv[1])
    if (not root_folder.exists()) and (not root_folder.is_dir()):
        print('Path incorrect')

    clean(root_folder)


if __name__ == "__main__":
    main()
