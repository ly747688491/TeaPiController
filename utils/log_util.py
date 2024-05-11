"""
@Project        ：TeaPiController
@File           ：log_util.py
@IDE            ：PyCharm
@Author         ：李延
@Date           ：2024/5/6 下午2:04
@Description    ：
"""
import os
import time

from loguru import logger

log_path = os.path.join(os.getcwd(), "logs")
if not os.path.exists(log_path):
    os.mkdir(log_path)

log_path_info = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}_info.log')
join = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}_error.log')
log_path_error = join

logger.add(
    log_path_info,
    rotation="50MB",
    level="INFO",
    encoding="utf-8",
    enqueue=True,
    compression="zip",
)

logger.add(
    log_path_error,
    rotation="50MB",
    level="ERROR",
    encoding="utf-8",
    enqueue=True,
    compression="zip",
)
