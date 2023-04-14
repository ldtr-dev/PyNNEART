# eeglab_download.py

# Project PyNNEART: Python Neural Network for EEG Artifact Removal Toolkit
# Semillero de Neuroinformática e Inteligencia Artificial (SNEIA)
# License: MIT license

import requests, os, zipfile


def download_eeglab(
    eeglab_download_path, file_path
):
    save_temp_path = os.path.join(file_path, save_folder_name)
    os.makedirs(save_temp_path, exist_ok=True)

    print("Downloading EEGLAB...")
    print("URL: (" + eeglab_download_path + eeglab_file_name + ")")
    r = requests.get(eeglab_download_path + eeglab_file_name)
    print("[OK]")
    with open(os.path.join(save_temp_path, eeglab_file_name), "wb") as f:
        print("Saving file...")
        print("PATH: (" + save_temp_path + ")")
        f.write(r.content)
        print("[OK]")
    print("EEGLAB downloaded successfully.")



def unzip_eeglab(
    eeglab_file_name,
    save_folder_name,
    extract_folder_name,
    file_path,
):
    save_temp_path = os.path.join(file_path, save_folder_name)
    extrac_temp_path = os.path.join(file_path, extract_folder_name)
    print("Unzipping EEGLAB...")
    print("FILE: (" + save_temp_path + eeglab_file_name + ")")
    with zipfile.ZipFile(save_temp_path + "/" + eeglab_file_name, "r") as zipObj:
        zipObj.extractall(extrac_temp_path)
    print("[OK]")
    print("EEGLAB unzipped successfully.")


def remove_temp_files(save_folder_name, file_path):
    save_temp_path = os.path.join(file_path, save_folder_name)
    print("Removing temporary files...")
    print("PATH: (" + save_temp_path + ")")
    for file in os.listdir(save_temp_path):
        os.remove(os.path.join(save_temp_path, file))
    print("[OK]")
    print("Temporary files removed successfully.")


if __name__ == "__main__":
    file_path = os.path.dirname(os.path.abspath(__file__))
    eeglab_download_path = "https://sccn.ucsd.edu/eeglab/currentversion/"
    eeglab_file_name = "eeglab_current.zip"
    save_folder_name = "temp"
    extract_folder_name = "versions"

    download_eeglab(eeglab_download_path, file_path)
    unzip_eeglab(
        eeglab_file_name,
        save_folder_name,
        extract_folder_name,
        file_path,
    )
    remove_temp_files(save_folder_name, file_path)

    print("EEGLAB installed successfully.")
