"""
@Project        ：TeaPiController
@File           ：serial_test.py
@IDE            ：PyCharm
@Author         ：李延
@Date           ：2024/5/6 下午2:13
@Description    ：
"""

import argparse
import threading

import serial


def read_serial():
    while True:
        try:
            if data := ser.readline():
                try:
                    decoded_data = data.decode("utf-8")
                    print(f"Received: {decoded_data}", end="")
                except UnicodeDecodeError:
                    hex_data = data.hex()
                    print(f"Received non-UTF-8 data: {hex_data}")
        except serial.SerialException as e:
            print(f"Serial read error: {e}")
            break


def main():
    global ser
    parser = argparse.ArgumentParser(description="Serial JSON Communication")
    parser.add_argument(
        "port", type=str, help="Serial port name (e.g., COM1 or /dev/ttyUSB0)"
    )

    args = parser.parse_args()
    print(f"Serial port: {args.port}")

    # 设置串口连接
    try:
        ser = serial.Serial(args.port, baudrate=9600, timeout=1)
        print("Connection successful.")
    except serial.SerialException as e:
        print(f"Failed to connect to {args.port}: {e}")
        return

    # 打印当前串口配置
    print(f"Serial configuration: {ser}")

    # 开启接收线程
    serial_recv_thread = threading.Thread(target=read_serial)
    serial_recv_thread.daemon = True
    serial_recv_thread.start()

    try:
        while True:
            command = input("Enter hex command (e.g., 34 or 23, without '0x'): ")
            if command.startswith("0x") or command.startswith("0X"):
                command_int = int(command.replace(" ", ""), 16)
                print(command_int)
                print(type(command_int))
                command_bytes = command_int.to_bytes(1, byteorder='big')
                ser.write(command_bytes + b"\n")
                print(f"Sent: {command}")
            else:
                bytes_data = bytes.fromhex(command.replace(" ", ""))
                ser.write(bytes_data)
    except Exception as e:
        print(e)
    finally:
        ser.close()
        print("Serial connection closed.")


if __name__ == "__main__":
    main()
