from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return render("mathFarmApp/index.html")

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return render(request, "mathFarmApp/index.html")