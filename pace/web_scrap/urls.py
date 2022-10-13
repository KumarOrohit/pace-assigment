from django.urls import path
from .views import WebScrapView


urlpatterns = [
    path('scrap-data', WebScrapView.as_view()),
]