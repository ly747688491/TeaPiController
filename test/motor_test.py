"""
@Project        ：TeaPiController 
@File           ：motor_test.py
@IDE            ：PyCharm 
@Author         ：李延
@Date           ：2024/5/6 下午2:15 
@Description    ：
"""
import time

from gpiozero import OutputDevice


def temp_control(ssid: int, operation_time: int):
    relay = OutputDevice(ssid)
    relay.on()
    print(f"GPIO {ssid} is now {'ON' if relay.is_active else 'OFF'}.")
    time.sleep(operation_time)
    relay.off()
    time.sleep(operation_time)
    print(f"GPIO {ssid} is now {'ON' if relay.is_active else 'OFF'}.")


if __name__ == "__main__":
    try:
        while True:
            relay_id = input("请输入GPIO编号：")
            operation_time = input("请输入操作时间（秒）：")
            relay_id = int(relay_id)
            operation_time = int(operation_time)
            temp_control(relay_id, operation_time)
    except Exception as e:
        print(e)
