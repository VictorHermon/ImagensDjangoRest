from rest_framework import viewsets
from imagens.serializers import ImagemSerializer
from imagens.models import Imagem


class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer
