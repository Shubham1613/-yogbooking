from django.shortcuts import render
from .models import Services
# Create your views here.
def index(request):
    services = Services.objects.all()
    return render(request, 'yogbookingapp/index.html',{'services' : services})
def services(request):
    services = Services.objects.all()

    return render(request,'yogbookingapp/services.html',{'services' : services})
def events(request):
    return render(request,'yogbookingapp/events.html')
