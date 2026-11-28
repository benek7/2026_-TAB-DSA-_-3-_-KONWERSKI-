from django.shortcuts import render, redirect, get_object_or_404
from .models import Wyciag, Cennik, Uzytkownik
from .models import DokumentPrzejazdu, Wyciag

def cennik(request):
    return render(request, 'core/kierownik/cennik.html')

def uzytkownicy(request):
    return render(request, 'core/kierownik/uzytkownicy.html')

def archiwum(request):
    return render(request, 'core/kierownik/archiwum.html')

def raporty_zarzadcze(request):
    return render(request, 'core/kierownik/raporty_zarzadcze.html')

def raporty_operacyjne(request):
    return render(request, 'core/kierownik/raporty_operacyjne.html')

def home(request):
    lifts = Wyciag.objects.all()
    tickets = DokumentPrzejazdu.objects.select_related("narciarz", "cennik").all()
    return render(request, "core/kierownik/home.html", {
        "lifts": lifts,
        "tickets": tickets,
    })

def kasjer_home(request):
    return render(request, 'core/kasjer/home.html')

def narciarz_home(request):
    return render(request, 'core/narciarz/home.html')

def zmien_stan_wyciagu(request, pk):
    if request.method == 'POST':
        wyciag = get_object_or_404(Wyciag, pk=pk)
        akcja = request.POST.get('akcja')
        if akcja == 'accept':
            wyciag.czyczynny = True
        elif akcja == 'reject':
            wyciag.czyczynny = False
        wyciag.save()
    return redirect('kierownik_home')

def cennik(request):
    pozycje = Cennik.objects.all()
    return render(request, 'core/kierownik/cennik.html', {'pozycje': pozycje})

def zmien_cene(request, pk):
    if request.method == 'POST':
        pozycja = get_object_or_404(Cennik, pk=pk)
        nowa_cena = request.POST.get('cena')
        if nowa_cena:
            pozycja.cena = nowa_cena.replace(',', '.')
            pozycja.save()
    return redirect('cennik')

def uzytkownicy(request):
    lista_uzytkownikow = Uzytkownik.objects.all()
    return render(request, 'core/kierownik/uzytkownicy.html', {
        'uzytkownicy': lista_uzytkownikow
    })

def archiwum(request):
    return render(request, 'core/kierownik/archiwum.html', {
        'uzytkownicy': Uzytkownik.objects.all(),
    })
def raporty_zarzadcze(request):
    liczba_uzytkownikow = Uzytkownik.objects.count()
    liczba_ofert = Cennik.objects.count()
    liczba_wyciagow = Wyciag.objects.count()
    return render(request, 'core/kierownik/raporty_zarzadcze.html', {
        'liczba_uzytkownikow': liczba_uzytkownikow,
        'liczba_ofert': liczba_ofert,
        'liczba_wyciagow': liczba_wyciagow,
    })

def raporty_operacyjne(request):
    wyciagi = Wyciag.objects.all()
    czynne = wyciagi.filter(czyczynny=True).count()
    nieczynne = wyciagi.filter(czyczynny=False).count()
    return render(request, 'core/kierownik/raporty_operacyjne.html', {
        'wyciagi': wyciagi,
        'czynne': czynne,
        'nieczynne': nieczynne,
    })

def kasjer_wydruk(request):
    klienci = Uzytkownik.objects.all()
    return render(request, 'core/kasjer/wydruk.html', {'klienci': klienci})

def narciarz_karnety(request):
    return render(request, 'core/narciarz/karnety.html')

def narciarz_bilety(request):
    return render(request, 'core/narciarz/bilety.html')

def narciarz_archiwum(request):
    return render(request, 'core/narciarz/archiwum.html')

def narciarz_kontakt(request):
    return render(request, 'core/narciarz/kontakt.html')