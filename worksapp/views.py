from django.shortcuts import render
from rest_framework.generics import ListAPIView
from . import models
from .serializers import MusicSerializer

class MusicView(ListAPIView):
    serializer_class = MusicSerializer

    def get_queryset(self):
        return models.MusicWorks.objects.filter(iswc=self.kwargs["iswc"])
