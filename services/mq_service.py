"""
@Project        ：TeaPiController
@File           ：mq_service.py
@IDE            ：PyCharm
@Author         ：李延
@Date           ：2024/5/6 下午2:04
@Description    ：rabbitMQ 服务 常驻订阅与设备号匹配的队列
"""
from contextlib import AbstractContextManager
from time import sleep

import pika
from pika.adapters.blocking_connection import BlockingChannel


class RabbitMQClient(AbstractContextManager):
    def __init__(self, callback):
        self.callback = callback
        self.connection = None
        self.channel = None

    def connect(self, rabbit_config) -> pika.BlockingConnection:
        while True:
            try:
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(
                        rabbit_config.host,
                        port=rabbit_config.port,
                        credentials=pika.PlainCredentials(
                            rabbit_config.rabbit_username, rabbit_config.rabbit_password
                        ),
                    )
                )
                return self.connection
            except pika.exceptions.AMQPConnectionError:
                print("Unable to connect to RabbitMQ server, retrying in 5 seconds...")
                sleep(5)

    def create_channel(self, raspberry_config) -> BlockingChannel:
        self.channel = self.connection.channel()
        self.channel.basic_consume(
            queue=raspberry_config.bind_id,
            on_message_callback=self.callback,
            auto_ack=True,
        )
        return self.channel

    def run(self) -> None:
        self.channel.start_consuming()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
