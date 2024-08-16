from django.contrib import admin
from django.urls import path, include
from area import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('area/', views.area_view, name='area'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('recurso/', views.recurso_view, name='recurso'),
    path('configuracoes/', views.configuracoes_view, name='configuracoes'),
]