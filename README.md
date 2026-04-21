# Dear Diary App

The "Dear Diary" app is meant to work as a digital diary application. The app enables users to create an account, Write into your daily diary with the help/inspiration of a daily prompt to guide your thought. You can then explore your earlier diary entries. The app has an admin account that can change the daily prompt, controll accounts and even delete anyones entry if needed.

## Documentation / Dokumentaatio

[Requiriments Specification / Vaatimusmäärittely](https://github.com/BjornKhermik10/ot-harjoitustyo/blob/master/dokumentaatio/misc/vaatimusmaarittely.md)

[WorkedHours Tracker / Työaikakirjanpito](https://github.com/BjornKhermik10/ot-harjoitustyo/blob/master/dokumentaatio/misc/tyoaikakirjanpito.md)

[Changelog](https://github.com/BjornKhermik10/ot-harjoitustyo/blob/master/dokumentaatio/misc/changelog.md)

[kayttoohje](https://github.com/BjornKhermik10/ot-harjoitustyo/blob/master/dokumentaatio/misc/English_instructions.md)

[Arkkitehtuuri](https://github.com/BjornKhermik10/ot-harjoitustyo/blob/master/dokumentaatio/misc/arkkitehtuuri.md)

[Testaus](https://github.com/BjornKhermik10/ot-harjoitustyo/blob/master/dokumentaatio/misc/testaus.md)

[Github Release](https://github.com/bjornkhermik10/ot-harjoitustyo/releases/latest)

## User Guide

## Starting the Program

Before starting the program, install the dependencies with the following command:

```
poetry install
```

Now the program can be started with the command:

```
poetry run invoke start
```

To generate a coverage report, use:

```
poetry run invoke coverage-report
```

To run lint checks, use:

```
poetry run invoke lint
```

In WSL, the task opens the report with Windows browser integration (explorer.exe).

## Creating a New User

From the login view, you can navigate to the "create new user" view by clicking the "Sign up" button.

A new user is created by entering the required details into the input fields and clicking the "Sign up" button. If the user creation is successful, you will be redirected to the home view.

## Logging In

The application opens to a home view where you can choose between the "create user" view or the login view. 

You can log in by entering an existing username into the input field and clicking the "Login" button.

## Daily prompt page

Write your daily journal entry with the help of the daily prompt quote

Submit your entry

## My entries page

Scroll through your entries in chronological order and delete them if needed

