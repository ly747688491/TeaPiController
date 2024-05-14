"""
@Project        ：TeaPiController
@File           ：http_service.py
@IDE            ：PyCharm
@Author         ：李延
@Date           ：2024/5/6 下午2:04
@Description    ：
"""
from seeting import settings


class HttpService:
    def __init__(self):
        self.base_url = settings.SERVER_API
