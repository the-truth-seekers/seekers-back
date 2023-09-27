from services.helpers import clean_text
from utils.modelos import modelo_vect, modelo_predicao


class Predict:
    def __init__(self):
        pass

    @staticmethod
    def predict_news(texto):
        texto_tratado = clean_text(texto)
        texto_vetorizado = modelo_vect.transform([texto_tratado])
        resultado = modelo_predicao.predict(texto_vetorizado)

        return resultado

    @staticmethod
    def predict_news_proba(texto):
        texto_tratado = clean_text(texto)
        texto_vetorizado = modelo_vect.transform([texto_tratado])
        resultado = modelo_predicao.predict_proba(texto_vetorizado)

        return resultado
