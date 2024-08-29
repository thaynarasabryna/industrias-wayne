from django.contrib import admin
from django.urls import path, include
from area import views
from .views import RecursoListView, RecursoCreateView, RecursoUpdateView, RecursoDeleteView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('area/', views.area_view, name='area'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('recurso/', views.recurso_view, name='recurso'),
    path('recursos/', RecursoListView.as_view(), name='recursos_list'),
    path('recursos/add/', RecursoCreateView.as_view(), name='recurso_add'),
    path('recursos/<int:pk>/edit/', RecursoUpdateView.as_view(), name='recurso_edit'),
    path('recursos/<int:pk>/delete/', RecursoDeleteView.as_view(), name='recurso_delete'),
    path('configuracoes/', views.configuracoes_view, name='configuracoes'),
]
