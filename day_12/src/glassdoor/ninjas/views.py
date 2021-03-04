from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import Developer,Skill

def index(request):
    devs = Developer.objects.all()
    context = {
        'devs' : devs
    }
    return render(request, 'ninja/index.html', context)

def details(request, dev_id):
    dev = get_object_or_404(Developer, pk=dev_id)
    return render(request, 'ninja/details.html', {'dev':dev})

def developers(request,skill):
    devs = Developer.objects.filter(skill__name=skill)
    context = {
        'devs' : devs
    }
    return render(request, 'ninja/developers.html', context)