"""linkedin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from linkedin.database.views import scrapping
# from linkedin.scrapping import views
# from linkedin.scrapping.views import scrap_endereco
from django.contrib import admin
from django.urls import path
from scrapping import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.scrap),
    path('scrap_endereco', views.scrap_endereco),
    path('scrap_maranhao', views.scrap_saude_maranhao),
    path('diretor', views.diretor_empresas)
]
