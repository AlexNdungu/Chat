from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import logout


# Create your views here.

def base(request):
    return render(request, 'base.html')

#the fron page 
def front(request):
    return render(request, 'front.html')

#sign in
def sign(request):
    return render(request, 'sign.html')

#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/front/')        