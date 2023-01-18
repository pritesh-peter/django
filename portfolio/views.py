from django.views.generic import TemplateView
from django.shortcuts import render

# here we are following the convention provided by Django
# IndexPageView vanne class call garyo vane index.html pathauxa

class IndexPageView(TemplateView):
    template_name = "index.html"

def index(request):
    return render(request,"index.html")