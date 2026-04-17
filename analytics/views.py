from django.shortcuts import render, redirect

def analytics(request):
    return render(request, 'analytics/home.html')