# Hour of code 2017 - Python3 using Flask + Peewee + Telepot

Sample of simple web service using Python3 with Flask, Peewee and Telepot for Hour of Code of 2017.

## Structure

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
    7. Upload files for user comments
2. Persistence with _peewee_
    1. Comment class
    2. Create database of SQLite
    3. Add method to write comments into database
    4. Add method to retrieve comments from database
    5. Link database with flask
3. Connect to Telegram using _telepot_
    1. Create bot using [@BotFather](https://telegram.me/BotFather)
    2. Hello World with telepot using webhooks sample (each time a user talks to bot, it answers 'Hello World')
    3. User class for telegram users' persistence (name, alias, profile image)
    4. Create function to add comments from telegram by:
        ```
        /newcomment <comment>
        ```
    5. Add function to accept images as comments
