from django.shortcuts import render

from .models import DokumentPrzejazdu, Wyciag


def home(request):
    lifts = Wyciag.objects.all()
    tickets = DokumentPrzejazdu.objects.select_related("narciarz", "cennik").all()
    return render(request, "core/home.html", {
        "lifts": lifts,
        "tickets": tickets,
    })
