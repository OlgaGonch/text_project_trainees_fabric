import nltk
import pymorphy2
nltk.download("stopwords")
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("russian")
russian_stopwords = stopwords.words("russian")
morph = pymorphy2.MorphAnalyzer()

def stemming_text(text):
    for sym in punctuation:
        text = text.replace(sym, ' ')
    tokens = text.lower()
    tokens = tokens.split()
    tokens = [stemmer.stem(token) for token in tokens if token not in russian_stopwords \
              and token != " "]
    text = " ".join(tokens)

    return text


def lemmatize_text(text):
    for sym in punctuation:
        text = text.replace(sym, ' ')
    tokens = text.lower()
    tokens = tokens.split()
    res = list()
    tokens = [morph.parse(token)[0].normal_form for token in tokens if token not in russian_stopwords \
              and token != " "]
    text = " ".join(tokens)

    return text


def make_preprocessing_with_stemming(source_file_path, ready_file_path):
    with open(source_file_path) as f:
        lines = f.readlines()

    file = open(ready_file_path, "wb")

    i = 0
    for line in lines:
        new_line = stemming_text(line[8:])
        file.write((str(i) + ' |text ' + new_line + '\n').encode())
        i += 1

    file.close()


def make_preprocessing_with_lemmatization(source_file_path, ready_file_path):
    with open(source_file_path) as f:
        lines = f.readlines()

    file = open(ready_file_path, "wb")

    i = 0
    for line in lines:
        new_line = lemmatize_text(line[8:])
        file.write((str(i) + ' |text ' + new_line + '\n').encode())
        i += 1

    file.close()
