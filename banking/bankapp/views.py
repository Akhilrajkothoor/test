from django.shortcuts import render

# Create your views here.
from bankapp.models import Banking
from . forms import ServiceForm
import banking
from tkinter import *
from tkinter import messagebox


def demo(request):

   return render(request,"index.html")

def done(request):

   return render(request,"done.html")


def add_bank_details(request):
   if request.method == "POST":
      name = request.POST.get('name', )
      email = request.POST.get('email', )
      mobile = request.POST.get('mobile', )
      date_of_birth = request.POST.get('date_of_birth', )
      address = request.POST.get('address', )
      district = request.POST.get('district', )
      branch= request.POST.get('branch', )
      account_type = request.POST.get('account_type', )
      service_required = request.POST.get('service_required', )

      banking = Banking(name=name,email=email,mobile=mobile,address=address,date_of_birth=date_of_birth,district=district,branch=branch,account_type=account_type,service_required=service_required)
      banking.save()
   return render(request,'service.html')