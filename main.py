from controllers.router import init_router
from seeting import RabbitMQconfig, RaspberryConfig
from services.mq_service import RabbitMQClient
from utils.log_util import logger


def initialize_system():
    init_rabbit()
    logger.info("系统启动完成，等待指令...")


def init_rabbit():
    raspberry = RaspberryConfig
    rabbit = RabbitMQconfig

    with RabbitMQClient(callback) as mq_service:
        mq_service.connect(rabbit)
        mq_service.create_channel(raspberry)
        mq_service.run()


def init_seeting():
    pass


def callback(ch, method, properties, body):
    init_router(ch, method, properties, body)


if __name__ == "__main__":
    initialize_system()
    logger.info("系统启动完成，等待指令...")
