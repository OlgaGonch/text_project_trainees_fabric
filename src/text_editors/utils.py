from string import punctuation
import pymorphy2
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


def lemmatize_text(text):
    for sym in punctuation:
        text = text.replace(sym, ' ')
    tokens = text.lower()
    tokens = tokens.split()
    res = list()
    morph = pymorphy2.MorphAnalyzer()
    russian_stopwords = stopwords.words("russian")
    tokens = [morph.parse(token)[0].normal_form for token in tokens if token not in russian_stopwords \
              and token != " "]
    text = " ".join(tokens)

    return text


def stemming_text(text):
    stemmer = SnowballStemmer("russian")
    russian_stopwords = stopwords.words("russian")
    for sym in punctuation:
        text = text.replace(sym, ' ')
    tokens = text.lower()
    tokens = tokens.split()
    tokens = [stemmer.stem(token) for token in tokens if token not in russian_stopwords \
              and token != " "]
    text = " ".join(tokens)

    return text
