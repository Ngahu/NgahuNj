from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from projects.models import Project


class HomeView(View):
    """
    Description:Render the home landing page of the project\n
    """

    def get(self, request, *args, **kwargs):
        template_name = 'main/index.html'
        featured_projects = Project.objects.filter(featured=True)
        context = {
            "featured_projects": featured_projects
        }
        return render(request, template_name, context)
