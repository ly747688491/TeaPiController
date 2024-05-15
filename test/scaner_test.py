"""
@Project        ：TeaPiController 
@File           ：scaner_test.py
@IDE            ：PyCharm 
@Author         ：李延
@Date           ：2024/5/6 下午2:14 
@Description    ：
"""
import sys

import evdev

print(sys.executable)
# 首先，找到扫码器的设备文件
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    print(device.path, device.name, device.phys)

# 使用识别出的扫码器设备路径
scanner_path = "/dev/input/event5"
scanner = InputDevice(scanner_path)

输出扫描到的二维码
print(f"Listening for QR codes on {scanner.path}...")
for event in scanner.read_loop():
    if event.type == ecodes.EV_KEY:
        data = categorize(event)
        if data.keystate == 1:  # 只处理按键按下的事件
            print(data.keycode)
