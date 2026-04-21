# Käyttöohje

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Nyt ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```

Coverage-raportin saa luotua komennolla:

```bash
poetry run invoke coverage-report
```
lint tarkistus onnistuu komennolla:

```
poetry run invoke lint
```

WSL-ymparistossa raportti avataan Windowsin selaimeen explorer.exe:n kautta.

## Kirjautuminen

Sovellus käynnistyy aloitusnäkymä josta voit valita luokäyttäjänäkymän tai kirjautumisnäkymän:

Kirjautuminen onnistuu kirjoittamalla olemassaoleva käyttäjätunnus sekä syötekenttään ja painamalla "Login"-painiketta.

## Uuden käyttäjän luominen

Kirjautumisnäkymästä on mahdollista siirtyä uuden käyttäjän luomisnäkymään panikkeella "Sign up".

Uusi käyttäjä luodaan syöttämällä tiedot syötekenttiin ja painamalla "Sign up"-painiketta:

Jos käyttäjän luominen onnistuu, siirrytään siirrytään aloitusnäkymään.

## Päivittäinen päiväkirjamerkintä

Kirjoita päivittäinen päiväkirjamerkintäsi päivän "quoten" avustuksella

Tallenna päivittäinen päiväkirjamerkintäsi

## Minun päiväkirjamerkinnät

Voit katso edelliset päivä kirja merkintäsi, järjestetty julkaisuajan mukaan

Voit poistaa niitä tarvittaessa
