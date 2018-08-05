from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('inventarios/', views.inventarios, name='inventarios'),
]