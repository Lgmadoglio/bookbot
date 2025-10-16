def get_book_text(path):
    file_contents = ""

    with open(path, encoding = "utf-8") as f:
        file_contents = f.read()

    return file_contents

def get_word_count(text):
    words = text.split()
    word_count = len(words)

    return word_count

def get_char_count(text_raw):
    text = text_raw.lower()
    char_count = {}
    for c in text:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    
    return char_count
