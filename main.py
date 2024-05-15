from controllers.router import init_router
from setup.setup_config import setup_config
from setup.setup_database import init_create_table
from utils.log_util import logger


def initialize_system():
    logger.info("系统启动中...")
    init_create_table()
    setup_config()

    # init_rabbit()
    logger.info("系统启动完成，等待指令...")


def callback(ch, method, properties, body):
    init_router(ch, method, properties, body)


if __name__ == "__main__":
    initialize_system()
