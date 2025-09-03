import os
from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406343224',
        'name': 'Galih Nur Rizqy',
        'class': 'PBP E'
    }
    current_directory = os.getcwd()
    print(current_directory)

    return render(request, "main.html", context)