"""
@Project        ：TeaPiController
@File           ：setup_database.py
@IDE            ：PyCharm
@Author         ：李延
@Date           ：2024/5/13 下午4:34
@Description    ：
"""

from contextlib import contextmanager

from loguru import logger

from core.database import Base, SessionLocal, engine
from models.base import ConfigModel, DeviceModel, MachineModel


@contextmanager
def get_db_pro():
    """
    每一个请求处理完毕后会关闭当前连接,不同的请求使用不同的连接
    :return:
    """
    current_db = SessionLocal()
    try:
        yield current_db
    finally:
        current_db.close()


def init_create_table():
    """
    应用启动时初始化数据库连接
    :return:
    """
    logger.info("初始化数据库连接...")
    Base.metadata.create_all(bind=engine)
    logger.info("数据库连接成功")


get_db = get_db_pro
