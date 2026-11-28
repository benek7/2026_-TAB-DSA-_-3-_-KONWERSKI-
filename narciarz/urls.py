"""
URL configuration for narciarz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('kierownik/', views.home, name='kierownik_home'),
    path('kierownik/cennik/', views.cennik, name='cennik'),
    path('kierownik/uzytkownicy/', views.uzytkownicy, name='uzytkownicy'),
    path('kierownik/archiwum/', views.archiwum, name='archiwum'),
    path('kierownik/raporty/zarzadcze/', views.raporty_zarzadcze, name='raporty_zarzadcze'),
    path('kierownik/raporty/operacyjne/', views.raporty_operacyjne, name='raporty_operacyjne'),
    path('wyciag/<int:pk>/stan/', views.zmien_stan_wyciagu, name='zmien_stan_wyciagu'),
    path('kasjer/', views.kasjer_home, name='kasjer_home'),
    path('narciarz/', views.narciarz_home, name='narciarz_home'),
    path('kierownik/cennik/<int:pk>/zmien-cene/', views.zmien_cene, name='zmien_cene'),
    path('kasjer/wydruk/', views.kasjer_wydruk, name='kasjer_wydruk'),
    path('narciarz/karnety/', views.narciarz_karnety, name='narciarz_karnety'),
    path('narciarz/bilety/', views.narciarz_bilety, name='narciarz_bilety'),
    path('narciarz/archiwum/', views.narciarz_archiwum, name='narciarz_archiwum'),
    path('narciarz/kontakt/', views.narciarz_kontakt, name='narciarz_kontakt'),
]