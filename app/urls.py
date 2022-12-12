from django.urls import path
from .views import *

urlpatterns=[
    path("", homePage.as_view(), name="home"),
    path("about/", aboutPage.as_view(), name="about"),
    path("contact/", contactPage.as_view(), name="contact"),
    path("my_team/", my_teamPage.as_view(), name="my team"),
    path("reklama/", reklamaPage.as_view(), name="reklaam"),
]