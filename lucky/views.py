from django.shortcuts import render

# Create your views here.

def venky(request):
    d={'address':'banglore','mobile':9505154793}
    return render(request,'venky.html',context=d)