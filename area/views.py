from django.shortcuts import render

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

