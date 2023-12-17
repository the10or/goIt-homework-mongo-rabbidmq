from faker import Faker

import connect

from bson import ObjectId
import connect_queue

from part_2.model import Contact

fake = Faker()
channel = connect_queue.channel


def produce(number_of_contacts):
    for i in range(number_of_contacts):
        contact = Contact(
            full_name=fake.name(),
            email=fake.email(),
            is_email_sent=False,
        )
        contact.save()
        contact_id = contact.id

        channel.basic_publish(
            exchange="", routing_key="email_queue", body=str(ObjectId(contact_id))
        )


if __name__ == '__main__':
    print('Producer started...')
    produce(20)
    print('Producer finished...')
