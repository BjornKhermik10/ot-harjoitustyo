# Testausdokumentti

## Yksikkö- ja integraatiotestaus
Projektin varsinaiset testit löytyvät "src/tests"-hakemistosta. Tällä hetkellä siellä on yksi testitiedosto: "user_service_test.py".

Testit jakautuvat pääosin yksikkötesteihin. Niissä testataan käyttäjän rekisteröintiä ja kirjautumista, tyhjien ja varattujen tunnusten käsittelyä, välilyöntien trimmausta, olemattoman käyttäjän kirjautumista, merkintöjen lisäämistä ja hakemista sekä poistamista.

Mukana on myös yksi integraatiotesti, joka tarkistaa, että data säilyy tiedostopohjaisen tietokannan yli, kun käytössä ovat "Database", "repository" ja "UserService"kerrokset yhdessä.

Coverage-raportti luodaan komennolla:

```bash
poetry run invoke coverage-report
```

## Järjestelmätestaus
