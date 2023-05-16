from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view

from .serializers import NoticiaSerializer
from .serializers import ResultadoSerializer
from .models import Resultado, Noticia


@api_view(['GET'])
def Consulta(request):    
    if request.method == 'GET': 
        url = request.query_params.get('url', None)
        if url is not None:
            try:
                noticia = Noticia.objects.get(link=url)
                resultado = Resultado.objects.filter(noticias=noticia)
                resultado_serializer = ResultadoSerializer(resultado, many=True)
                return JsonResponse({'data':resultado_serializer.data}, safe=False)
            except Noticia.DoesNotExist:
                noticia = Noticia.objects.create(link=url)    
        return JsonResponse({'data':[]}, safe=False)

