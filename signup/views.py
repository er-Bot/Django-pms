from django.shortcuts import render

def signup_form(request):
    return render(request, "signup/signup_form.html")

def signin_form(request):
    return render(request, "signup/signin_form.html")
