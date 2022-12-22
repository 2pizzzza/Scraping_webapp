from django.shortcuts import render

def homepage(request):
    return render(request, 'scraping/home.html')
