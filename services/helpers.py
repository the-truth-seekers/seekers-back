from utils.constantes import Constantes
import re


def clean_text(value):
    x = re.sub(r"(#\S+)|(@\S+)|(http\S+)", "", value).lower().replace('.', '').replace(';', '') \
        .replace('-', '').replace(':', '').replace(')', '').strip().split()
    x = [palavra.lower() for palavra in x if palavra.isalpha() and palavra not in Constantes.STOPWORDS and not len(palavra) <= 2]
    return ' '.join(x)
