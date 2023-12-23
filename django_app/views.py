from django.shortcuts import render
from .models import data
from django.core.paginator import Paginator

def index(request):
    return render(request, 'index.html')

def home(request):
    dt = data.objects.all()
    paginator = Paginator(dt,10)
    page_number = request.GET.get('page')
    dt = paginator.get_page(page_number)
    return render(request, 'home.html', {'data': dt})