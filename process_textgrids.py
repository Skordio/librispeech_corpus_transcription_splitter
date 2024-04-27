import os
import glob
from tqdm import tqdm  # Import tqdm for the progress bar

def parse_textgrid(filepath):
    """ Parses a TextGrid file and extracts interval data. """
    words = []
    times = []
    with open(filepath, 'r', encoding='utf-8') as file:
        intervals = False
        for line in file:
            if 'item [2]' in line:
                break
            if "intervals [" in line:
                intervals = True
            if intervals:
                if "text =" in line:
                    word = line.split('=')[-1].strip().strip('"')
                    words.append(word)
                elif "xmax =" in line:
                    time = line.split('=')[-1].strip()
                    times.append(time)
                elif "item [" in line or "intervals: size" in line:
                    intervals = False
    return words, times

def process_directory(root_dir):
    """ Process each directory and subdirectory containing TextGrid files. """
    # Walk through the directory structure
    for subdir, dirs, files in tqdm(os.walk(root_dir), desc="Processing directories", unit="dir"):
        textgrid_files = glob.glob(os.path.join(subdir, '*.TextGrid'))
        if not textgrid_files:
            continue

        # Extract speaker and book IDs from the directory structure
        parts = subdir.split(os.sep)
        if len(parts) < 3:
            continue
        speaker_id = parts[-2]
        book_id = parts[-1]

        output_path = os.path.join(subdir, f"{speaker_id}_{book_id}.alignment.txt")
        with open(output_path, 'w', encoding='utf-8') as outfile:
            # print(f"Processing {output_path}")
            for i, textgrid_file in enumerate(textgrid_files):
                file_name = os.path.basename(textgrid_file)
                file_title = file_name.split('.')[0]
                speaker_id, book_id, clip_id = file_title.split('_')
                words, times = parse_textgrid(textgrid_file)
                words_line = ','.join(['' if word == "" else word.upper() for word in words])
                times_line = ','.join(times)
                outfile.write(f'{speaker_id}_{book_id}_{clip_id} "{words_line}" "{times_line}"')
                if not i == len(textgrid_files) - 1:
                    outfile.write('\n')

# Example usage:
root_directory = "D:\\Github\\335_project\\datasets\\spanish_datasets\\LibriSpeech\\train-other-500"
process_directory(root_directory)
