"""
Syntactic example of kafka usage for the brave of all syntactic examples
"""

from common_py_lib.entities.Formatter import TextAnsiFormatter
from confluent_kafka import Consumer, Producer


def create_node():
    pass


class PPConsumer:
    consumer_conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'pp_group',
        'auto.offset.reset': 'earliest'
    }

    def __init__(self):
        self.consumer = Consumer(self.consumer_conf)
        self.consumer.subscribe(['log_topic'])

    def start(self):
        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    TextAnsiFormatter.prRed(f'Consumer error: {msg.error()}')
                else:
                    TextAnsiFormatter.prRed(msg.value.decode('utf-8'))
        except KeyboardInterrupt:
            self.consumer.close()


class PPProducer:
    producer_conf = {'bootstrap.servers': 'localhost:9092'}

    def __init__(self):
        self.producer = Producer(self.producer_conf)

    def callback(self, error, message):
        if error:
            TextAnsiFormatter.prRed(f'Ошибка при отправке: {error}')

    def produce(self, msg):
        self.producer.produce('log_topic', value=msg)
        self.producer.flush()


class Kafka_controller:

    def __init__(self):
        self.producer = PPProducer()
        self.consumer = PPConsumer()
