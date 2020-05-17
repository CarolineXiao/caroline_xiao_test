#!/usr/bin/env python
import pika
from random import seed
from random import randint
from LRUCache import *

try:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    channel.queue_declare(queue='queue')

    # Create an LRUCache object
    capacity = input("Please enter the cache capacity: ")
    ttl = input("Please enter the ttl in seconds (default = None): ")
    if ttl:
        cache = LRUCache(int(capacity), int(ttl))
    else:
        cache = LRUCache(int(capacity))
except:
    print("Error: something went wrong.")


def on_request(ch, method, props, body):
    key = int(body)

    print(" [.] %s" % key)
    response = cache.get(key)

    # if the key is not found in cache, set a random value to the key and store the pair in cache
    if response == "Not Found":
        seed()
        val = randint(0, 100)
        cache.set(key, val)
        response = val

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

    print("Current cache: ", end='')
    cache.printCache()

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='queue', on_message_callback=on_request)

print(" [x] Awaiting for requests")
channel.start_consuming()