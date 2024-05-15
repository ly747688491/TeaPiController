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
            # 尝试将response内容转换为JSON格式，如果不是JSON格式则返回原始内容
            response_data = response.json()
            # Check if 'code' and 'msg' are in the response_data
            if "code" in response_data and "msg" in response_data:
                return {
                    "status_code": response_data[
                        "code"
                    ],  # Use the 'code' from the response_data
                    "data": response_data.get(
                        "data", {}
                    ),  # Safely get the 'data' or return an empty dict
                    "msg": response_data["msg"],  # Use the 'msg' from the response_data
                }
        except ValueError:
            # If there is a ValueError, it means that the response is not in JSON format
            response_data = response.text

        # If the above try block fails, return the original status code, response text, and headers
        return {
            "status_code": response.status_code,  # The original HTTP status code
            "data": response_data,  # The raw response text if not JSON
            "headers": response.headers,  # The response headers
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
