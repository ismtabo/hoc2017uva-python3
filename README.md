# Hour of code 2017 - Python3 using Flask + Peewee + Telepot

Sample of simple web service using Python3 with Flask, Peewee and Telepot for Hour of Code of 2017.

## How to follow this tutorial

First of all, download at your machine:
```
$ git clone https://github.com/ismtabo/hoc2017uva-python3.git
```

Install its only dependence:
- Virtualenv: 
    - To install on UNIX/Linux systems, execute below command:
        ```
        $ sudo apt install virtualenv
        ```
    - To install on other OS, follow instructions at official web page: https://virtualenv.pypa.io/en/stable/

## Structure of tutorial

Sample has three different parts:

1. Web service using Flask:
    1. Prepare virtual environment or use global system:
        1. Virtual environment:
            ```
            $ virtualenv -p python3 venv
            $ source venv/bin/activate
            (venv) $ pip install -r requirements.txt
            ```
        2. Using already installed packages 
    2. _Hello World_ using Flask
    3. Dynamic content with templates.
    4. Comment structure using:
        - Templates
        - `collections.namedtuple`
    5. List of comments
    6. Form to post comments
2. Persistence with _peewee_
    1. Comment class
    2. Create database of SQLite
    3. Add method to write comments into database
    4. Add method to retrieve comments from database
    5. Link database with flask
3. Connect to Telegram using _telepot_
    1. Create bot using [@BotFather](https://telegram.me/BotFather)
    2. Hello World with telepot using webhooks sample (each time a user talks to bot, it answers 'Hello World')
    3. Create function to add comments from telegram by:
        ```
        /newcomment <comment>
        ```
## Getting started into the tutorial

Below tags identify several steps of the tutorial, you can show them at: https://github.com/ismtabo/hoc2017uva-python3/releases

To start with the tutorial, checkout first one with below command:
```
$ git checkout <tag_name>
```

For first step, it will be:
```
$ git checkout v1.1-flask-templates
```

In case, you want to advance in the tutorial but you already have done changes in the code, first discard this changes with:
```
$ git stash save --keep-index # Add changes to stash
$ git stash drop              # Discard stash
```
Ànd then, checkout correct step's tag.


Contributors
---
- Ismael Taboada: [ismtabo](https://github.com/ismtabo)
