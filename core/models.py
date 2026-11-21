from django.db import models


class Uzytkownik(models.Model):
    class Role(models.TextChoices):
        KIEROWNIK = "Kierownik", "Kierownik"
        KASJER = "Kasjer", "Kasjer"
        NARCIARZ = "Narciarz", "Narciarz"

    login = models.CharField(max_length=50, unique=True)
    haslo = models.CharField(max_length=255)
    rola = models.CharField(max_length=20, choices=Role.choices)

    class Meta:
        db_table = "uzytkownik"
        verbose_name = "Użytkownik"
        verbose_name_plural = "Użytkownicy"

    def __str__(self):
        return self.login


class SlownikTypow(models.Model):
    nazwatypu = models.CharField(max_length=50)
    czaswaznoscidni = models.PositiveIntegerField(null=True, blank=True)
    liczbazjazdow = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        db_table = "slowniktypow"
        verbose_name = "Słownik typu"
        verbose_name_plural = "Słownik typów"

    def __str__(self):
        return self.nazwatypu


class Cennik(models.Model):
    slowniktypow = models.ForeignKey(SlownikTypow, on_delete=models.PROTECT, related_name="pozycje_cennika")
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    obowiazujeod = models.DateTimeField()
    obowiazujedo = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "cennik"
        verbose_name = "Pozycja cennika"
        verbose_name_plural = "Cennik"

    def __str__(self):
        return f"{self.slowniktypow.nazwatypu} - {self.cena} zł"


class DokumentPrzejazdu(models.Model):
    class Status(models.TextChoices):
        AKTYWNY = "Aktywny", "Aktywny"
        WYGLASLY = "Wygasly", "Wygasły"
        ZABLOKOWANY = "Zablokowany", "Zablokowany"
        ZARCHIWIZOWANY = "Zarchiwizowany", "Zarchiwizowany"

    kodqr = models.CharField(max_length=100, unique=True)
    czaszakupu = models.DateTimeField()
    status = models.CharField(max_length=20, choices=Status.choices)
    kasjer = models.ForeignKey(Uzytkownik, on_delete=models.PROTECT, null=True, blank=True, related_name="obsluzone_dokumenty")
    narciarz = models.ForeignKey(Uzytkownik, on_delete=models.PROTECT, null=True, blank=True, related_name="dokumenty_przejazdu")
    cennik = models.ForeignKey(Cennik, on_delete=models.PROTECT, related_name="dokumenty")

    class Meta:
        db_table = "dokumentprzejazdu"
        verbose_name = "Dokument przejazdu"
        verbose_name_plural = "Dokumenty przejazdu"

    def __str__(self):
        return self.kodqr


class Bilet(models.Model):
    dokument = models.OneToOneField(DokumentPrzejazdu, on_delete=models.CASCADE, primary_key=True, related_name="bilet")
    pozostalezjazdy = models.PositiveIntegerField()

    class Meta:
        db_table = "bilet"
        verbose_name = "Bilet"
        verbose_name_plural = "Bilety"

    def __str__(self):
        return f"Bilet {self.dokument_id}"


class Karnet(models.Model):
    dokument = models.OneToOneField(DokumentPrzejazdu, on_delete=models.CASCADE, primary_key=True, related_name="karnet")
    waznydo = models.DateTimeField()

    class Meta:
        db_table = "karnet"
        verbose_name = "Karnet"
        verbose_name_plural = "Karnety"

    def __str__(self):
        return f"Karnet {self.dokument_id}"


class Wyciag(models.Model):
    nazwa = models.CharField(max_length=100)
    wysokosc = models.PositiveIntegerField()
    godzinaotwarcia = models.TimeField()
    godzinazamkniecia = models.TimeField()
    czyczynny = models.BooleanField(default=True)

    class Meta:
        db_table = "wyciag"
        verbose_name = "Wyciąg"
        verbose_name_plural = "Wyciągi"
        ordering = ["nazwa"]

    def __str__(self):
        return self.nazwa


class Przejazd(models.Model):
    czasodbicia = models.DateTimeField()
    dokument = models.ForeignKey(DokumentPrzejazdu, on_delete=models.PROTECT, related_name="przejazdy")
    wyciag = models.ForeignKey(Wyciag, on_delete=models.PROTECT, related_name="przejazdy")

    class Meta:
        db_table = "przejazd"
        verbose_name = "Przejazd"
        verbose_name_plural = "Przejazdy"

    def __str__(self):
        return f"{self.wyciag.nazwa} - {self.czasodbicia}"
