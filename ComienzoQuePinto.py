from peewee import*

db = SqliteDatabase('quePintoUser.db')

class Person(Model):
    name = CharField()
    dni = TextField()
    email = TextField()
    password = TextField()

    class Meta:
        database = db

class Event(Model):
    nameEvent = CharField()
    organizer = CharField()
    category = CharField()
    description = TextField()
    galery =
    city = CharField()
    department = CharField()
    country = CharField()
    gpslength =
    gpslatitude =
    startDate =
    endingDate = 


def create_and_connect():
    db.connect()
    db.create_tables([Person],safe=True)
