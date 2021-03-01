def get_devanagari_words(file='index_txt'):
    """Generator that yields hindi Devanagari words from the 
    word-net data selected from https://www.cfilt.iitb.ac.in/wordnet/
    """
    with open(file) as f:
        encountered_first_char = False
        for line in f.readlines():
            word = line.strip().split()[0]
            if word=='अ':
                encountered_first_char=True
            if not encountered_first_char:
                continue
            else:
                yield word.strip()