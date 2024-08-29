from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Recurso

# Create your views here.
def login_view(request):
    return render(request, "login.html")

def area_view(request):
    return render(request, 'area.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def recurso_view(request):
    return render(request, 'recurso.html')

def configuracoes_view(request):
    return render(request, 'configuracoes.html')

class RecursoListView(ListView):
    model = Recurso
    template_name = 'recursos.html'

class RecursoCreateView(CreateView):
    model = Recurso
    fields = ['descricao', 'localidade', 'quantidade', 'situacao']
    template_name = 'recurso_form.html'

class RecursoUpdateView(UpdateView):
    model = Recurso
    fields = ['descricao', 'localidade', 'quantidade', 'situacao']
    template_name = 'recurso_form.html'

class RecursoDeleteView(DeleteView):
    model = Recurso
    template_name = 'recurso_confirm_delete.html'
    success_url = reverse_lazy('recursos_list')