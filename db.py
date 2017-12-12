from peewee import SqliteDatabase, Model, CharField, TextField

db = SqliteDatabase('comments.db')

class Comment(Model):
    title = CharField()
    content = TextField()

    class Meta:
        database = db

db.connect()

if not Comment.table_exists():
    Comment.create_table()
