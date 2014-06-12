from django.http.response import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
from django.views.generic.list import ListView
from users.models import Worker


class UsersView(ListView):
    model = Worker
    template_name = "index.html"
