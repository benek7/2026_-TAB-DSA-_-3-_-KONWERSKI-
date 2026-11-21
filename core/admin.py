from django.contrib import admin

from .models import (
    Bilet,
    Cennik,
    DokumentPrzejazdu,
    Karnet,
    Przejazd,
    SlownikTypow,
    Uzytkownik,
    Wyciag,
)


@admin.register(Uzytkownik)
class UzytkownikAdmin(admin.ModelAdmin):
    list_display = ("login", "rola")
    list_filter = ("rola",)
    search_fields = ("login",)


@admin.register(SlownikTypow)
class SlownikTypowAdmin(admin.ModelAdmin):
    list_display = ("nazwatypu", "czaswaznoscidni", "liczbazjazdow")


@admin.register(Cennik)
class CennikAdmin(admin.ModelAdmin):
    list_display = ("slowniktypow", "cena", "obowiazujeod", "obowiazujedo")
    list_filter = ("slowniktypow",)


@admin.register(DokumentPrzejazdu)
class DokumentPrzejazduAdmin(admin.ModelAdmin):
    list_display = ("kodqr", "status", "narciarz", "kasjer", "cennik", "czaszakupu")
    list_filter = ("status",)
    search_fields = ("kodqr", "narciarz__login")


@admin.register(Bilet)
class BiletAdmin(admin.ModelAdmin):
    list_display = ("dokument", "pozostalezjazdy")


@admin.register(Karnet)
class KarnetAdmin(admin.ModelAdmin):
    list_display = ("dokument", "waznydo")


@admin.register(Wyciag)
class WyciagAdmin(admin.ModelAdmin):
    list_display = ("nazwa", "wysokosc", "godzinaotwarcia", "godzinazamkniecia", "czyczynny")
    list_filter = ("czyczynny",)
    search_fields = ("nazwa",)


@admin.register(Przejazd)
class PrzejazdAdmin(admin.ModelAdmin):
    list_display = ("dokument", "wyciag", "czasodbicia")
    list_filter = ("wyciag",)
