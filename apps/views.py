from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView

from apps.models import User


# Create your views here.

class IndexView(ListView):
    model = User
    template_name = 'apps/index.html'
    context_object_name = 'users'

class UserDeleteView(DeleteView):
    model = User
    context_object_name = 'user'
    success_url = reverse_lazy('index_page')

class UserUpdateView(UpdateView):
    model = User
    template_name = 'apps/update_user.html'
    fields = ['name', 'address', 'category']
    context_object_name = 'user'
    success_url = reverse_lazy('index_page')