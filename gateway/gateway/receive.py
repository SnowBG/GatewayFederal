#!/usr/bin/env python
"""
Este programa recebe e exibe mensagens de uma fila única.

Módulos:
    pika, sys, os
Métodos:
    callback
"""

import pika
import sys
import os


def main():
    """
    Função principal que conecta à fila determinada.

    Variáveis:
        - connection: estipula qual endereço de servidor será usado.
        - channel: instância do canal a ser conectado.
    Parâmetros:
        - queue: define qual fila será consumida.
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost')
    )
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        """Esse metodo recebe as mensagens da fila e imprime na tela\
        a mensagem recebida. É um método padrão da lib 'pika'."""
        print(" [x] Received %r" % body)

    channel.basic_consume(
        queue='hello', auto_ack=True, on_message_callback=callback
    )

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
