from django.shortcuts import render,redirect

from mainapp.models import Enquiry

# Create your views here.
def index(request):
    return render(request,"index.html")

def savedata(request):
    user_name = request.POST['user_name']
    phn_num = request.POST['phn_num']
    email_id = request.POST['user_name']
    data = Enquiry(user_name = user_name,phn_num = phn_num,email_id = email_id)
    data.save()
    return redirect (index)