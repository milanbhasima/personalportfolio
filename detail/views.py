from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import BlogPost
from .forms import ContactForm
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django import forms


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

# def blog(request):
#     template = loader.get_template('blog.html')
#     return HttpResponse(template.render())

# def contact(request):
#     template = loader.get_template('contact.html')
#     return HttpResponse(template.render())




def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully!")
            return redirect("contact")

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

def blog(request):

    posts = BlogPost.objects.filter(
        status="published"
    )

    return render(
        request,
        "blog.html",
        {"posts": posts}
    )

def blog_detail(request, slug):

    post = get_object_or_404(
        BlogPost,
        slug=slug,
        status="published"
    )

    post.view_count += 1
    post.save(update_fields=["view_count"])

    return render(
        request,
        "blog.html",
        {"post": post}
    )