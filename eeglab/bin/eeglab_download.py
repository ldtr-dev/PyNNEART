# eeglab_download.py

# Project PyNNEART: Python Neural Network for EEG Artifact Removal Toolkit
# Semillero de Neuroinformática e Inteligencia Artificial (SNEIA)
# License: MIT license

import requests, os


def download_eeglab(
    eeglab_download_path="https://sccn.ucsd.edu/eeglab/currentversion/",
    eeglab_file_name="eeglab_current.zip",
    save_folder_name="temp",
):
    save_temp_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), save_folder_name)
    print("Downloading EEGLAB...")
    print("URL: (" + eeglab_download_path + eeglab_file_name + ")")
    r = requests.get(eeglab_download_path + eeglab_file_name)
    print("[OK]")
    with open(save_temp_path + "/" + eeglab_file_name, "wb") as f:
        print("Saving file...")
        print("PATH: (" + save_temp_path + ")")
        f.write(r.content)
        print("[OK]")
    print("EEGLAB downloaded successfully.")

if __name__ == "__main__":
    download_eeglab()
