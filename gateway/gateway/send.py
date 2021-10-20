#!/usr/bin/env python

"""
Esse programa envia uma mensagem única para a fila.

Módulos:
    pika
Variáveis:
    - connection: estipula qual endereço de servidor será usado.
    - channel: instância do canal a ser conectado.
Parâmetros:
    - queue: define qual fila será consumida.
"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello belly!')

print(" [x] Sent 'Hello World'")

connection.close()
