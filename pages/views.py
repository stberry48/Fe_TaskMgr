from django.views.generic import TemplateView
from django.views import View



class HomePageView(TemplateView):
    template_name = "pages/home.html"

    class AboutPageView(TemplateView):
        template_name = "pages/about.html"
