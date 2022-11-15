from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ArtisteViewSet, SongViewSet, LyricViewSet

router = DefaultRouter()
router.register(r'artiste', ArtisteViewSet, basename='artiste')
router.register(r'song', SongViewSet, basename='song')
router.register(r'lyric', LyricViewSet, basename='lyric')

urlpatterns = [] + router.urls

# 127.0.0.1:8000/artiste
