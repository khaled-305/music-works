from django.urls import path
from .views import MusicView

urlpatterns = [
    path('music/<int:iswc>/', MusicView.as_view(), name='music'),
]