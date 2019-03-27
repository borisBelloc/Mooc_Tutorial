"""Disquaire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls import include, url

from store import views


urlpatterns = [
    url(r'^admin/', admin.site.urls), # r signifie q'uon va utiliser une expression regulière
    url(r'^store/', include('store.urls', namespace="store")), #toutes les urls du fichier url de l'app STORE, commenceront par "store"

    url(r'^$', views.index, name="index"),
        # ^on veut que toutes les urls vide envoie sur l'index
    


]




if settings.DEBUG: # on ne veut pouvoir acceder a la django debug toolbar que si le mode debug est activé
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns