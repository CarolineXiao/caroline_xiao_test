#!/usr/bin/env python
import pika
import uuid
import socket

class LRUClient(object):

    def __init__(self):
        try:
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='localhost'))
        except socket.gaierror:
            print("Error: Cannot connect to server. Node name or server name not found.")
            quit()
        else:
            try:
                self.channel = self.connection.channel()

                result = self.channel.queue_declare(queue='', exclusive=True)
                self.callback_queue = result.method.queue

                self.channel.basic_consume(
                    queue=self.callback_queue,
                    on_message_callback=self.on_response,
                    auto_ack=True)
            except:
                print("Error: something went wrong.")
                quit()

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, key):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(key))
        while self.response is None:
            self.connection.process_data_events()
        return self.response




client = LRUClient()

input = input("Enter request key: ")
print(" [x] Requesting " + input)
response = client.call(input)
print(" [.] Got " + str(response)[1:])