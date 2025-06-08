from django.urls import path
from .views import GetRandQuote

urlpatterns = [
    path('', GetRandQuote.as_view(), name='get-random-quote'),
]