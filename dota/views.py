from django.shortcuts import render

# Create your views here.
def dota(request):
    return render(request, 'dota.html')
