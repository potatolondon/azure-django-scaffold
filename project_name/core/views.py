from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "base.html"

home = HomeView.as_view()
