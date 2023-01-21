from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from cv.models import Skill,Message

# here we are following the convention provided by Django
# IndexPageView vanne class call garyo vane index.html pathauxa

class IndexPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["skill_list"] = Skill.objects.all()
        return context

def index(request):
    return render(request,"homepage")


def submit_message(request):
    if request.method=="POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        m = Message()
        m.name = name
        m.email = email
        m.subject = subject
        m.message = message

        m.save()

        return redirect('.')
    return redirect(request,'.',{})