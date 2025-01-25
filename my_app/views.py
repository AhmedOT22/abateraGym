from django.shortcuts import render

def home(request):
    return render(request, 'my_app/templates/index.html')
