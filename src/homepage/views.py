from django.shortcuts import render
from django.views import generic
# Create your views here.


class HomePage(generic.TemplateView):
    template_name = "hp/home_page.html"
    


def success_page(request):
    return render(
        request,
        template_name='hp/success.html'
    )