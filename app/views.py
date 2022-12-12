from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import *
# Create your views here.

class homePage(ListView):
    paginate_by = 2
    model= Post
    template_name="home.html"




class aboutPage(TemplateView):
    template_name="about.html"




class contactPage(CreateView):
    model = Contact
    template_name="contact.html"
    fields = "__all__"


class my_teamPage(TemplateView):
    template_name="my_team.html"
class reklamaPage(TemplateView):
    template_name="reklama.html"

