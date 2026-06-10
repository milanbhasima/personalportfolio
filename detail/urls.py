from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('resume', views.resume, name='resume'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path("blog", views.blog, name="blog_list"),

    # path(
    #     "blog/create/",
    #     views.create_post,
    #     name="create_post"
    # ),

    # path(
    #     "blog/<slug:slug>/",
    #     views.blog_detail,
    #     name="blog_detail"
    # ),
]
