from django.shortcuts import render, HttpResponse

# Create your views here.

def index_view(request):
    if request.user.is_authenticated:context = {'who': 'Admin',}
    else: context = {'who': 'Anonymous',}
    return render(request,'index.html',context)

