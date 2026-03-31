# Käyttöohje

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Jonka jälkeen suorita alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

Nyt ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```

## Kirjautuminen

Sovellus käynnistyy aloitusnäkymä josta voit valita luokäyttäjänäkymän tai kirjautumisnäkymän:

Kirjautuminen onnistuu kirjoittamalla olemassaoleva käyttäjätunnus sekä syötekenttään ja painamalla "Login"-painiketta.

## Uuden käyttäjän luominen

Kirjautumisnäkymästä on mahdollista siirtyä uuden käyttäjän luomisnäkymään panikkeella "Sign up".

Uusi käyttäjä luodaan syöttämällä tiedot syötekenttiin ja painamalla "Sign up"-painiketta:

Jos käyttäjän luominen onnistuu, siirrytään siirrytään aloitusnäkymään.
