from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm
# Create your views here.
from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('index1.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def resume(request):
    template = loader.get_template('resume.html')
    return HttpResponse(template.render())

def portfolio(request):
    template = loader.get_template('portfolio.html')
    return HttpResponse(template.render())

def blog(request):
    template = loader.get_template('blog.html')
    return HttpResponse(template.render())

# def contact(request):
#     template = loader.get_template('contact.html')
#     return HttpResponse(template.render())




def contact(request):
    if request.method == "POST":
        print('hello')
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully!")
            return redirect("contact")

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})