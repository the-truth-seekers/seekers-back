from rest_framework.decorators import api_view
from django.http import JsonResponse
from services.predict import Predict
import json


@api_view(['POST'])
def predicao(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        texto = data.get('texto')

        predict = Predict.predict_news(texto).tolist()[0]

        prob = Predict.predict_news_proba(texto)[0]
        probabilidades = {
            'fake': prob[0],
            'true': prob[1]
        }

        resposta_analisada = None

        if probabilidades['fake'] > 0.7:
            resposta_analisada = False

        if probabilidades['true'] > 0.7:
            resposta_analisada = True

        return JsonResponse({'resultado': predict, 'resposta_analisada': resposta_analisada, 'probabilidades': probabilidades})

    return JsonResponse({'error': 'Método não permitido'}, status=405)
