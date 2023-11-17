from rest_framework.decorators import api_view
from django.http import JsonResponse
from predict.services.predict import Predict
import json


@api_view(['POST'])
def predicao(request):
    print(request.method)
    if request.method == 'POST':
        modelo = request.GET.get('modelo', 'rnn')
        data = json.loads(request.body)
        texto = data.get('texto')

        if modelo == 'rnn':
            return Predict.predict_rnn(texto)
        elif modelo == 'randomForest':
            return Predict.predict_rf(texto)
        else:
            return JsonResponse({'error': 'Modelo não reconhecido'}, status=405)

    return JsonResponse({'error': 'Método não permitido'}, status=405)
