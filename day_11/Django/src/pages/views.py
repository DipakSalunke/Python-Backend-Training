from django.shortcuts import render
# Create your views here.

def home_view(request,*args,**kwargs):
    my_context = {
        "Country":"<b>Philippines</b>",
        "info":["+63","peso"]
    }
    return render(request,"home.html",my_context)