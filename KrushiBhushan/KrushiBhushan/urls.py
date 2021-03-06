"""KrushiBhushan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add/product/$', add_product),
    url(r'^all/product/$', get_all_products),
    url(r'^slider/$', slider),
    url(r'^gallery/$', gallery),
    url(r'^add/team/',AddTeam),
    url(r'^get/team/member/',get_team),
    url(r'^add/contact/',add_contact),
    url(r'^get/contact/',get_contact),
    url(r'^get/menu/',get_menu),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
