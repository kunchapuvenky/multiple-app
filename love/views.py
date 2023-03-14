from django.shortcuts import render

# Create your views here.
def amma(request):
    d={'name':'anusha','age':42}
    return render(request,'amma.html',context=d)