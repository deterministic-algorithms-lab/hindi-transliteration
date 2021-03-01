"""
Script to prepare tsv files with 
devanagari_word     romanized_version
"""
import argparse
from googletrans import Translator
import os
from pathlib import Path
from devanagari import get_devanagari_words

translator = Translator()

if __name__=='__main__':
    parser.add_argument('--write_file', type=str, required=True, help='File to write the transliterations to.')
    
    file_to_read = os.path.join(Path(os.path.realpath()).parent, 'index_txt')
    
    with open(args.write_file, 'w+') as f:
        for word in get_devanagari_words(file=file_to_read):
            transliteration = translator.translate('नाम', dest='en').extra_data['translation'][-1][-1]
            str_to_write = word+'\t'+transliteration+'\n'
            f.write(str_to_write)
