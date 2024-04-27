import os
import shutil
from tqdm import tqdm

def reorganize(source_dir, target_dir):
    # Prepare a list of files to be processed for progress tracking
    file_list = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_list.append((root, file))

    # Walk through all directories and files in the source directory
    for root, file in tqdm(file_list, desc="Reorganizing files"):
        file_path = os.path.join(root, file)
        
        file_name = file.split('.')[0]
        
        speaker_id = file_name.split('_')[0]
        section_id = file_name.split('_')[1]
        destination = os.path.join(target_dir, speaker_id, section_id)

        # Check if destination directory exists, create if not
        if not os.path.exists(destination):
            os.makedirs(destination)
        
        # Copy file to the new location
        shutil.copy(file_path, destination)

# Example usage
alignments_current_dir = 'D:\\Github\\335_project\\datasets\\spanish_datasets\\LibriSpeech\\librispeech_mfa_aligned'
alignments_new_dir = 'D:\\Github\\335_project\\datasets\\spanish_datasets\\LibriSpeech\\librispeech_mfa_aligned_reorganized'

reorganize(alignments_current_dir, alignments_new_dir)
