from controllers.router import init_router
from setup.setup_database import init_create_table
from utils.log_util import logger


def initialize_system():
    logger.info("系统启动中...")
    init_setting()
    init_create_table()
    # init_rabbit()
    logger.info("系统启动完成，等待指令...")


# def init_rabbit():
#     raspberry = RaspberryConfig
#     rabbit = RabbitMQconfig
#
#     with RabbitMQClient(callback) as mq_service:
#         mq_service.connect(rabbit)
#         mq_service.create_channel(raspberry)
#         mq_service.run()


def init_setting():
    pass


def callback(ch, method, properties, body):
    init_router(ch, method, properties, body)


if __name__ == "__main__":
    initialize_system()
