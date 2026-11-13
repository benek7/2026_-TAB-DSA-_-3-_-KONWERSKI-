CREATE TABLE Uzytkownik (
    id INT PRIMARY KEY,
    login VARCHAR(50) NOT NULL UNIQUE,
    haslo VARCHAR(255) NOT NULL,
    rola VARCHAR(20) NOT NULL CHECK (rola IN ('Kierownik', 'Kasjer', 'Narciarz'))
);

CREATE TABLE SlownikTypow (
    id INT PRIMARY KEY,
    nazwaTypu VARCHAR(50) NOT NULL,
    czasWaznosciDni INT,
    liczbaZjazdow INT
);

CREATE TABLE Cennik (
    id INT PRIMARY KEY,
    slownikTypow_id INT NOT NULL,
    cena DECIMAL(10, 2) NOT NULL,
    obowiazujeOd TIMESTAMP NOT NULL,
    obowiazujeDo TIMESTAMP,
    CONSTRAINT fk_cennik_slownik FOREIGN KEY (slownikTypow_id) REFERENCES SlownikTypow(id)
);

CREATE TABLE DokumentPrzejazdu (
    id INT PRIMARY KEY,
    kodQR VARCHAR(100) NOT NULL UNIQUE,
    czasZakupu TIMESTAMP NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('Aktywny', 'Zablokowany', 'Wygasly', 'Zarchiwizowany')),
    kasjer_id INT,
    narciarz_id INT,
    cennik_id INT NOT NULL,
    CONSTRAINT fk_dok_kasjer FOREIGN KEY (kasjer_id) REFERENCES Uzytkownik(id),
    CONSTRAINT fk_dok_narciarz FOREIGN KEY (narciarz_id) REFERENCES Uzytkownik(id),
    CONSTRAINT fk_dok_cennik FOREIGN KEY (cennik_id) REFERENCES Cennik(id)
);

CREATE TABLE Bilet (
    dokument_id INT PRIMARY KEY,
    pozostaleZjazdy INT NOT NULL,
    CONSTRAINT fk_bilet_dokument FOREIGN KEY (dokument_id) REFERENCES DokumentPrzejazdu(id) ON DELETE CASCADE
);

CREATE TABLE Karnet (
    dokument_id INT PRIMARY KEY,
    waznyDo TIMESTAMP NOT NULL,
    CONSTRAINT fk_karnet_dokument FOREIGN KEY (dokument_id) REFERENCES DokumentPrzejazdu(id) ON DELETE CASCADE
);

CREATE TABLE Wyciag (
    id INT PRIMARY KEY,
    nazwa VARCHAR(100) NOT NULL,
    wysokosc INT NOT NULL,
    godzinaOtwarcia VARCHAR(8) NOT NULL,
    godzinaZamkniecia VARCHAR(8) NOT NULL,
    czyCzynny SMALLINT DEFAULT 1 NOT NULL CHECK (czyCzynny IN (0, 1))
);

CREATE TABLE Przejazd (
    id INT PRIMARY KEY,
    czasOdbicia TIMESTAMP NOT NULL,
    dokument_id INT NOT NULL,
    wyciag_id INT NOT NULL,
    CONSTRAINT fk_przejazd_dokument FOREIGN KEY (dokument_id) REFERENCES DokumentPrzejazdu(id),
    CONSTRAINT fk_przejazd_wyciag FOREIGN KEY (wyciag_id) REFERENCES Wyciag(id)
);