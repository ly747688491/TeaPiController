"""
@Project        ：TeaPiController 
@File           ：mq_service_test.py
@IDE            ：PyCharm 
@Author         ：李延
@Date           ：2024/5/6 下午2:15 
@Description    ：
"""
import pika

from configs.env import RaspberryConfig, RassitMQconfig


def callback(ch, method, properties, body):
    print(f" [x] Received {properties}")
    print(f" [x] Received {method.routing_key}")
    print(f" [x] Received {body.decode()}")


def main():
    consumer_id = RaspberryConfig.bind_id

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            RassitMQconfig.host,
            port=RassitMQconfig.port,
            credentials=pika.PlainCredentials(
                RassitMQconfig.rabbit_username, RassitMQconfig.rabbit_password
            ),
        )
    )
    channel = connection.channel()

    print(f" [*] Waiting for messages for {consumer_id}. To exit press CTRL+C")
    channel.basic_consume(
        queue=consumer_id, on_message_callback=callback, auto_ack=True
    )

    channel.start_consuming()
