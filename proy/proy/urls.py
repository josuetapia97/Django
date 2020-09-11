"""proy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo_sencillo/',views.saludo),
    path('saludo_normal/',views.saludo_html),
    path('saludo_cargador/',views.saludo_html_cargador),
    path('saludo_shortcut/',views.saludo_render),
    path('saludo_herencia/',views.saludo_herencia),
    path('saludo_herencia2/',views.saludo_herencia2),
]
