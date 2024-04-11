from django.shortcuts import render
from datetime import datetime
x=datetime.now
# Create your views here.

def home(request):
    return render(request, 'index.html', {'date': x})
