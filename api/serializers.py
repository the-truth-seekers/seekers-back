from rest_framework import serializers

from .models import Noticia, Resultado


class NoticiaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Noticia
        fields = ('id', 'link')

    def __init__(self, instance=None, data=None, **kwargs):
        request = kwargs.get('context', {}).get('request')
        super().__init__(instance=instance, data=data, **kwargs, context={'request': request})

class ResultadoSerializer(serializers.HyperlinkedModelSerializer):
    noticias = NoticiaSerializer()

    class Meta:
        model = Resultado
        fields = ('id', 'titulo', 'resultado', 'fonte', 'noticias')

    def get_noticias(self, obj):
        noticias = obj.noticias.all()
        serializer = NoticiaSerializer(noticias, many=True)
        return serializer.data

    def __init__(self, instance=None, data=None, **kwargs):
        request = kwargs.get('context', {}).get('request')
        super().__init__(instance=instance, data=data, **kwargs, context={'request': request})