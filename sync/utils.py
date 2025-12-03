def save_words_to_txt(words, path):
    with open(path, "w", encoding="utf-8") as f:
        for w in words:
            f.write(w + "\n")


def load_txt_as_string(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()
