#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

import pika

credentials = pika.PlainCredentials('admin','123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.80.130',5672,'/',credentials))
channel = connection.channel()

channel.exchange_declare(exchange='Clogs',exchange_type='fanout')

result = channel.queue_declare(exclusive=True) #不指定queue名字，rabbit会随机分配一个名字，exclusive=True会在使用此queue的消费者断开后，自动将queue删除
queue_name = result.method.queue

channel.queue_bind(exchange='Clogs',
                   queue=queue_name)

def callback(ch,method,properties,body):
    print "Received %r" % (body,)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

print ' [*] Waiting for message. To exit press CTRL+C'
channel.start_consuming()
