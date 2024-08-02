from django.shortcuts import render

# Create your views here.
def registration(response):
    return render(response,"registration/templates/login.html")
    