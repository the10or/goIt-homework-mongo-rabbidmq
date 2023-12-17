from mongoengine import *


class Contact(Document):
    full_name = StringField()
    email = EmailField()
    is_email_sent = BooleanField(default=False)
    meta = {'collection': 'contacts'}
