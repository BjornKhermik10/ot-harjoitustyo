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

´´´mermaid

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

´´´

´´´mermaid

class UI{
    +start()
    +_open_signup()
    +_open_login()
    +_open_daily_prompt()
    +_open_my_entries()
}

class UserService{
    +register(username, password) bool
    +login(username, password) bool
    +add_entry(username, prompt, content) bool
    +get_entries_for_user(username) list
    -_hash_password(password) str
    -_verify_password(password, password_hash) bool
}

class UserRepository{
    +create(username, password_hash) bool
    +find_by_username(username) dict
}

class EntryRepository{
    +create(user_id, prompt, content)
    +find_for_user(user_id) list
}

class Database{
    +get_connection()
}

´´´