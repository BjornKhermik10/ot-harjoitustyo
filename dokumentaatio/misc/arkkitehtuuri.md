# Arkkitehtuurikuvaus

## Rakenne

## käyttöliittymä
Käyttöliittymään kuuluu 4 näkymää toistaiseksi:
- sign up
- login
- startpage
- logged in page
- Daily prompt page
- my entries page

## Sovelluslogiikka
Sovellukseen on nyt lisätty tietokanta sqlite3, jossa on käyttäjät ja "journal entries"

Sovelluksen tietomallin muodostavat luokat

```mermaid
    classDiagram
    User "1" --> "*" Entry

    class User{
        id
        username
        password_hash
    }

    class Entry{
        id
        user_id
        prompt
        content
        created_at
    }
```
ohjelman osien suhdetta kuvaava kaavio

```mermaid
classDiagram
    UI --> UserService
    UserService --> UserRepository
    UserService --> EntryRepository
    UserRepository --> Database
    EntryRepository --> Database

    class UI
    class UserService
    class UserRepository
    class EntryRepository
    class Database
```
Kirjautumisen sekvenssikaavio

```mermaid
sequenceDiagram
    actor Käyttäjä
    participant UI
    participant UserService
    participant UserRepository
    participant Database

    Käyttäjä->>UI: Syöttää käyttäjätunnuksen ja salasanan
    Käyttäjä->>UI: Painaa LOGIN
    UI->>UserService: login(username, password)
    UserService->>UserRepository: find_by_username(username)
    UserRepository->>Database: Hae käyttäjä rivinä
    Database-->>UserRepository: Käyttäjä tai ei löytynyt
    UserRepository-->>UserService: user / None
    UserService-->>UI: true / false
```

Päiväkirjamerkinnän luomisen sekvenssikaavio

```mermaid
sequenceDiagram
    actor Käyttäjä
    participant UI
    participant UserService
    participant EntryRepository
    participant Database

    Käyttäjä->>UI: Kirjoittaa tekstin päivän "promptin" avulla
    Käyttäjä->>UI: Painaa Preview
    Käyttäjä->>UI: Syöttää otsikon / tarkistaa oikein kirjotuksen
    Käyttäjä->>UI: Painaa Publish
    UI->>UserService: add_entry(username, prompt, content, title)
    UserService->>EntryRepository: create_entry(user_id, prompt, content, title)
    EntryRepository->>Database: Tallenna merkintä riviksi
    Database-->>EntryRepository: Merkintä tallennettu
    EntryRepository-->>UserService: true / false
    UserService-->>UI: true / false
    UI-->>Käyttäjä: Näytä onnistumisviesti
```
