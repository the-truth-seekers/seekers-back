from django.http import JsonResponse

from predict.services.helpers import clean_text, limpar_texto, lematize_sentence
from utils.modelos import modelo_vect, modelo_predicao_rf, modelo_tokenizer, modelo_pad_sequences, modelo_predicao_rnn


class Predict:
    def __init__(self):
        pass

    @staticmethod
    def resposta_analisada(probabilidades):
        resposta_analisada = None

        if probabilidades['fake'] > 0.7:
            resposta_analisada = False

        if probabilidades['true'] > 0.7:
            resposta_analisada = True

        return resposta_analisada

    @staticmethod
    def predict_news_rf(texto):
        texto_tratado = clean_text(texto)
        texto_vetorizado = modelo_vect.transform([texto_tratado])
        resultado = modelo_predicao_rf.predict(texto_vetorizado)

        return resultado

    @staticmethod
    def predict_news_proba_rf(texto):
        texto_tratado = clean_text(texto)
        texto_vetorizado = modelo_vect.transform([texto_tratado])
        resultado = modelo_predicao_rf.predict_proba(texto_vetorizado)

        return resultado

    @staticmethod
    def predict_rf(texto: str) -> JsonResponse:
        predict = Predict.predict_news_rf(texto).tolist()[0]
        prob = Predict.predict_news_proba_rf(texto)[0]

        probabilidades = {
            'fake': prob[0],
            'true': prob[1]
        }

        resposta_analisada = Predict.resposta_analisada(probabilidades)

        return JsonResponse({'resultado': predict, 'resposta_analisada': resposta_analisada,
                             'probabilidades': probabilidades})

    @staticmethod
    def predict_rnn(texto: str) -> JsonResponse:
        max_len = 300

        news = limpar_texto(texto)
        news = lematize_sentence(news)
        seq = modelo_tokenizer.texts_to_sequences([news])
        padded_seq = modelo_pad_sequences(seq, maxlen=max_len)

        prediction = modelo_predicao_rnn.predict(padded_seq)

        true_prob = prediction[0][0]

        resultado = 'true' if true_prob > 0.5 else 'fake'

        probabilidades = {
            'fake': float(1 - true_prob),
            'true': float(true_prob)
        }

        resposta_analisada = Predict.resposta_analisada(probabilidades)

        return JsonResponse({'resultado': resultado, 'resposta_analisada': resposta_analisada,
                             'probabilidades': probabilidades})
