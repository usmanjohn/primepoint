from django.shortcuts import render

# Create your views here.
def practice_home(request):
    return render(request, 'practice/practice_home.html')