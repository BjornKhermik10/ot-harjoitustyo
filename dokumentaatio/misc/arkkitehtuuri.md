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
ohjelman luokkien suhdetta kuvaava luokkakaavio

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
