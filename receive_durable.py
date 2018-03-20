#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

import pika

credentials = pika.PlainCredentials('admin','123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.80.130',5672,'/',credentials))
channel = connection.channel()

channel.queue_declare(queue='durable',durable=True)

def callback(ch,method,properties,body):
    print "Received %r" % (body,)
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(callback,
                      queue="durable",
                      #no_ack=True
                      )

print ' [*] Waiting for message. To exit press CTRL+C'
channel.start_consuming()
