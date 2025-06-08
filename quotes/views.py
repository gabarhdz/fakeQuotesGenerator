from django.shortcuts import render
from django.http import JsonResponse
from .models import Quote,Author
from django.views import View
import random
# Create your views here.

class GetRandQuote(View):
    def get(self, request):
        quotes = Quote.objects.all()
        authors = Author.objects.all()
        data = [{"author":author.name,"text":quote.text} for quote in quotes for author in authors]
        random_quote = random.choice(data)
        print(random_quote)
        return JsonResponse(random_quote,safe=False, status=200)
        