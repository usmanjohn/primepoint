from django.shortcuts import render
from .models import Panda

# Create your views here.
def panda_home(request):
    panders = Panda.objects.all()
    context = {'panders': panders}
    return render(request, 'panda/panda_list.html', context)