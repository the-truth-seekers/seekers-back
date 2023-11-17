from utils.constantes import Constantes
import spacy
import re


def clean_text(value):
    x = re.sub(r"(#\S+)|(@\S+)|(http\S+)", "", value).lower().replace('.', '').replace(';', '') \
        .replace('-', '').replace(':', '').replace(')', '').strip().split()
    x = [palavra.lower() for palavra in x if
         palavra.isalpha() and palavra not in Constantes.STOPWORDS and not len(palavra) <= 2]
    return ' '.join(x)


def lematize_sentence(sentence):
    nlp = spacy.load("pt_core_news_sm")
    doc = nlp(sentence)
    return ' '.join([word.lemma_ for word in doc])


def limpar_texto(value):
    value = re.sub(r"(#\S+)|(@\S+)|(http\S+)", "", value)
    for char in ['.', ';', '-', ':', ')']:
        value = value.replace(char, '')
    return value.strip().lower()
