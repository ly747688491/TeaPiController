"""
@Project        ：TeaPiController
@File           ：http_service.py
@IDE            ：PyCharm
@Author         ：李延
@Date           ：2024/5/6 下午2:04
@Description    ：
"""

import requests
from requests import RequestException


class HttpService:
    def __init__(self, url, data=None, headers=None):
        self.url = url
        self.data = data
        if headers is None:
            self.headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
        else:
            self.headers = headers

    def _process_response(self, response):
        """统一处理返回信息"""
        try:
            response_data = response.json()
            if "code" in response_data and "msg" in response_data:
                return {
                    "status_code": response_data["code"],
                    "data": response_data.get("data", {}),
                    "msg": response_data["msg"],
                }
        except ValueError:
            response_data = response.text
        return {
            "status_code": response.status_code,
            "data": response_data,
            "headers": response.headers,
        }

    def get(self):
        """发送GET请求"""
        try:
            response = requests.get(self.url, headers=self.headers)
            return self._process_response(response)
        except RequestException as e:
            return {"error": str(e)}

    def post(self):
        """发送POST请求"""
        try:
            response = requests.post(self.url, data=self.data, headers=self.headers)
            return self._process_response(response)
        except RequestException as e:
            return {"error": str(e)}

    def put(self):
        """发送PUT请求"""
        try:
            response = requests.put(self.url, data=self.data, headers=self.headers)
            return self._process_response(response)
        except RequestException as e:
            return {"error": str(e)}

    def delete(self):
        """发送DELETE请求"""
        try:
            response = requests.delete(self.url, headers=self.headers)
            return self._process_response(response)
        except RequestException as e:
            return {"error": str(e)}
