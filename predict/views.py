from rest_framework.decorators import api_view
from django.http import JsonResponse
import json

from services.predict import Predict


@api_view(['POST'])
def predicao(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        texto = data.get('texto')
        predict = Predict.predict_news(texto)

        return JsonResponse({'resultado': predict.tolist()[0]})

    return JsonResponse({'error': 'Método não permitido'}, status=405)
