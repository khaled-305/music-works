from django.shortcuts import render
from rest_framework.generics import ListAPIView
from . import models
from .serializers import MusicSerializer

class MusicView(ListAPIView):
    #permission_classes = [AllowAny]
    serializer_class = MusicSerializer

    def get_queryset(self):
        return models.MusicWorks.objects.filter(iswc=self.kwargs["iswc"])
