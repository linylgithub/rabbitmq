#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

import pika
import sys

credentials = pika.PlainCredentials('admin','123456')

connection = pika.BlockingConnection(pika.ConnectionParameters(
            '192.168.80.130',5672,'/',credentials))
channel = connection.channel()

channel.exchange_declare(exchange='Clog',exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='Clogs',
                      routing_key='',
                      body=message)

print "[x] Sent 'Hello World!'"
connection.close()

