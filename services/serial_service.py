"""
@Project        ：TeaPiController 
@File           ：serial_service.py
@IDE            ：PyCharm 
@Author         ：李延
@Date           ：2024/5/13 下午2:48 
@Description    ：
"""
import threading

import serial


class SerialService:

    def __init__(self, serial_port, baudrate):
        self.serial_port = serial_port
        self.baudrate = baudrate
        self.ser = None

        try:
            self.ser = serial.Serial(self.serial_port, baudrate=self.baudrate, timeout=1)
        except serial.SerialException as e:
            raise e

        # 开启接收线程
        serial_recv_thread = threading.Thread(target=self.read_serial)
        serial_recv_thread.daemon = True
        serial_recv_thread.start()

    def write_serial(self, data):
        try:
            while True:
                if data.startswith("0x") or data.startswith("0X"):
                    data_int = int(data.replace(" ", ""), 16)
                    data_bytes = data_int.to_bytes(1, byteorder='big')
                    self.ser.write(data_bytes + b"\n")
                else:
                    bytes_data = bytes.fromhex(data.replace(" ", ""))
                    self.ser.write(bytes_data)
        except Exception as e:
            print(e)
        finally:
            self.ser.close()
            print("Serial connection closed.")

    def read_serial(self):
        while True:
            try:
                if data := self.ser.readline():
                    try:
                        decoded_data = data.decode("utf-8")
                        print(f"Received: {decoded_data}", end="")
                    except UnicodeDecodeError:
                        hex_data = data.hex()
                        print(f"Received non-UTF-8 data: {hex_data}")
            except serial.SerialException as e:
                print(f"Serial read error: {e}")
                break
