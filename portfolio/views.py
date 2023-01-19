from django.views.generic import TemplateView
from django.shortcuts import render
from cv.models import Skill

# here we are following the convention provided by Django
# IndexPageView vanne class call garyo vane index.html pathauxa

class IndexPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["skill_list"] = Skill.objects.all()
        return context

def index(request):
    return render(request,"index.html")