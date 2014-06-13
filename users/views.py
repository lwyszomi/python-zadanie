from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
# Create your views here.
from django.views.generic.list import ListView
from users.models import Worker


class UsersView(ListView):
    model = Worker
    template_name = "index.html"

class UsersCreate(CreateView):
    model = Worker
    template_name = "worker_form.html"
    success_url = "/"

class UsersUpdate(UpdateView):
    model = Worker
    template_name = "worker_form.html"

class UsersDelete(DeleteView):
    model = Worker
    success_url = reverse_lazy('worker-detail')
    template_name = "worker_form.html"