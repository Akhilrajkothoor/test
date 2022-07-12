from . import views
from django.urls import path
app_name="bankapp"

urlpatterns = [

    path('',views.demo,name='demo'),
    path('add_bank_details/',views.add_bank_details,name='add_bank_details'),
path('done/',views.done,name='done'),


    ]