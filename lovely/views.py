from django.shortcuts import render

# Create your views here.
def lohith(request):
    d={'name':'lohith','age':3}
    return  render(request,'lohith.html',context=d)