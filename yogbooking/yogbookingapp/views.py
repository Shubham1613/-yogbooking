from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'yogbookingapp/index.html')
def services(request):
    return render(request,'yogbookingapp/services.html')
def events(request):
    return render(request,'yogbookingapp/events.html')
