#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

import pika

credentials = pika.PlainCredentials('admin','123456')

connection = pika.BlockingConnection(pika.ConnectionParameters(
            '192.168.80.130',5672,'/',credentials))
channel = connection.channel()

#声明queue
channel.queue_declare(queue='durable',durable=True)

#n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='durable',
                      body='Hello durable!',
                      properties=pika.BasicProperties(
                          delivery_mode=2, # make message persistent
                      )
                      )

print "[x] Sent 'Hello durable!'"
connection.close()

