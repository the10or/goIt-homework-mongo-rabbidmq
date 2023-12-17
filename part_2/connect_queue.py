import pika
import configparser

config = configparser.ConfigParser()
config.read(r'..\config.ini')

host = config.get('RABBITMQ', 'host')
port = config.get('RABBITMQ', 'port')
user = config.get('RABBITMQ', 'user')
password = config.get('RABBITMQ', 'pass')


credentials = pika.PlainCredentials(user, password)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=host, port=port, credentials=credentials)
)
channel = connection.channel()
channel.queue_declare(queue="email_queue")