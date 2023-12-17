import connect
from part_2.model import Contact
import connect_queue


def callback(ch, method, properties, body):
    contact_id = body.decode()

    contact = Contact.objects(id=contact_id).first()
    send_email(contact)
    if contact:
        contact.is_email_sent = True
        contact.save()


def send_email(contact):
    # print(contact.email)
    pass


if __name__ == '__main__':
    print('Consumer started')
    channel = connect_queue.channel
    try:
        channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
        print('Consumer stopped')
