"""
@Project        ：TeaPiController 
@File           ：gpio_test.py
@IDE            ：PyCharm 
@Author         ：李延
@Date           ：2024/5/6 下午2:12 
@Description    ：
"""
from utils.operation_utils import temp_control

if __name__ == "__main__":
    while True:
        relay_id = input("请输入GPIO编号：")
        operation_time = input("请输入操作时间（秒）：")
        if relay_id == "exit":
            break
        relay_id = int(relay_id)
        operation_time = int(operation_time)
        temp_control(relay_id, operation_time)
