from django.shortcuts import render
from Guest.models import *
# Create your views here.

def homepage(request):
    return render(request,'Guest/Homepage.html')

def myprofile(request):
    user=tbl_user.objects.get(id=1)
    return render(request,'Guest/MyProfile.html',{'user':user})

def portfolio(request):
    return render(request,'Guest/Portfolio.html')

def edit_profile(request):
    user=tbl_user.objects.get(id=1)
    if request.method=="POST":
        user.user_name=request.POST.get("txt_name")
        user.user_email=request.POST.get("txt_email")
        user.user_contact=request.POST.get("txt_contact")
        user.user_address=request.POST.get("txt_address")
        user.save()
        return render(request,'Guest/EditProfile.html',{'user':user})
    else:
        return render(request,'Guest/EditProfile.html',{'user':user})