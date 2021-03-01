"""
Script to prepare tsv files with 
devanagari_word     romanized_version
"""
import argparse
from googletrans import Translator
import os
from pathlib import Path
from devanagari import get_devanagari_words
import time

translator = Translator()

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--write_file', type=str, required=True, help='File to write the transliterations to.')
    args = parser.parse_args()

    file_to_read = os.path.join(Path(os.path.realpath(__file__)).parent, 'index_txt')
    
    with open(args.write_file, 'w+') as f:
        for word in get_devanagari_words(file=file_to_read):
            transliteration = translator.translate(word, dest='en').extra_data['translation'][-1][-1]
            str_to_write = word+'\t'+transliteration+'\n'
            f.write(str_to_write)
            time.sleep(1)