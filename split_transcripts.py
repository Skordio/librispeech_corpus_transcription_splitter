import argparse, os

def parse_args():
    parser = argparse.ArgumentParser(description='Split the transcripts into separate files')
    parser.add_argument('-t', '--transcripts', type=str, default='transcripts.txt', help='Path to the transcripts file')
    parser.add_argument('-o', '--output', type=str, default='output', help='Path to the output directory')
    parser.add_argument('--overwrite', action='store_true', default=True, help='Overwrite the existing transcription files')
    return parser.parse_args()

def process_file(transcripts_file, transcripts_dir, overwrite=True):
    with open(transcripts_file, encoding='utf8') as trans_file:
        lines = trans_file.readlines()
        
        speakers_processed = []
        
        sections_processed = []
        
        for line in lines:
            id_section = line.split()[0]
            
            words = line.split()[1:]
            
            id_section = id_section.split('_')
            
            speaker_id = id_section[0]
            section_id = id_section[1]
            clip_id = id_section[2]
            
            speaker_and_section = f'{speaker_id}-{section_id}'
                    
            dir_path = f'{transcripts_dir}\{speaker_id}\{section_id}'
            file_path = f'{dir_path}\{speaker_id}-{section_id}.trans.txt'
            
            if speaker_id not in speakers_processed:
                speakers_processed.append(speaker_id)
                print(f'Processing speaker {speaker_id}')
                
            if speaker_and_section not in sections_processed:
                sections_processed.append(speaker_and_section)
        
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)
            
                if overwrite and os.path.exists(file_path):
                    os.remove(file_path)
                
            with open(file_path, 'a', encoding='utf8') as new_file:
                new_file.write(f'{speaker_id}-{section_id}-{clip_id} {" ".join(words).upper()}\n')

if __name__ == '__main__':
    args = parse_args()
    
    transcripts_file = os.path.join(os.getcwd(), args.transcripts)
    transcripts_dir = os.path.join(os.path.dirname(transcripts_file), args.output)
    
    process_file(transcripts_file, transcripts_dir, args.overwrite)