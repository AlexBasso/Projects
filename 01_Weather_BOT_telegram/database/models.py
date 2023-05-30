from datetime import datetime

import peewee as pe

db = pe.SqliteDatabase('history.db')


class ModelBase(pe.Model):
    """
    Child class that inherits from peewee.Model and acts parent class for History. MetaClass links to db.
    Attr:
        created_at: peewee.DateTimeFiled, at the moment of instantiation saves current time.
    """
    created_at = pe.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        database = db


class History(ModelBase):
    """
    Child class of ModelBase that represents History table in DB.
    Attr:
        sender_id: unique id of message sender is 'int'
        name: name of the message sender is 'str'
        command: command (/command) of the message sender is 'str'
        request: request (/command request) of the message sender is 'str', can be Null.
        bot_response: bot response of the message sender is 'str'
        last_city: last city for which bot command was successfully used.
    """
    sender_id = pe.IntegerField()
    name = pe.TextField()
    command = pe.TextField()
    request = pe.TextField(null=True)
    bot_response = pe.TextField()
    last_city = pe.TextField(default='Chisinau')
