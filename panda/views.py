from django.shortcuts import render

# Create your views here.
def panda_home(request):
    return render(request, 'panda/panda_home.html')