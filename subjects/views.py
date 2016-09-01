from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests


@login_required
def index(request):
    r = requests.get()
    return render(request, 'subjects/index.html')
