from django.shortcuts import get_object_or_404

# Create your views here.
from .models import Developer
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

#class-based generic views

class IndexList(ListView):
    template_name = 'ninja/index.html'
    context_object_name = 'devs'

    def get_queryset(self):
        return Developer.objects.all()
    
class DetailsList(ListView):
    model = Developer
    template_name = 'ninja/details.html'
    context_object_name = 'dev'
    def get_queryset(self):
        return Developer.objects.filter(pk=self.kwargs['dev_id']).first()

class DevelopersList(ListView):
    model = Developer
    template_name = 'ninja/developers.html'
    context_object_name = 'devs'   
    def get_queryset(self):
        return Developer.objects.filter(skill__name=self.kwargs['skill'])
    
#Function-Based Views

def level(request, dev_id):
    dev = get_object_or_404(Developer, pk=dev_id)
    select = dev.skill_set.get(pk=request.POST['skill'])
    select.level += 1
    select.save()
    return HttpResponseRedirect(reverse('ninjas:details',args=(dev_id,)))