"""
@Project        ：TeaPiController 
@File           ：slide_rail.py
@IDE            ：PyCharm 
@Author         ：李延
@Date           ：2024/5/6 下午2:16 
@Description    ：
"""
import time

from gpiozero import InputDevice, OutputDevice, PWMOutputDevice


class RailSystem:
    def __init__(
            self,
            pul_pin,
            dir_pin,
            start_sensor_pin,
            end_sensor_pin,
            steps_per_revolution,
            pulses_per_step,
    ):
        self.pul = PWMOutputDevice(pul_pin, frequency=1000)  # 步进电机的脉冲控制引脚
        self.dir = OutputDevice(dir_pin)  # 步进电机的方向控制引脚
        self.start_sensor = InputDevice(start_sensor_pin)  # 起始位置的传感器
        self.end_sensor = InputDevice(end_sensor_pin)  # 结束位置的传感器
        self.steps_per_revolution = steps_per_revolution  # 每圈的步进数
        self.pulses_per_step = pulses_per_step  # 每步所需的脉冲数
        self.position = 0  # 当前位置计数器

    def move_to_position(self, target_position):
        steps_needed = target_position - self.position
        direction = "cw" if steps_needed > 0 else "ccw"
        self.rotate_motor(abs(steps_needed), direction)

    def rotate_motor(self, steps, dir):
        print(f"Motor direction is now {'CW' if dir == 'cw' else 'CCW'}.")
        self.dir.on() if dir == "cw" else self.dir.off()

        # 生成脉冲信号
        for _ in range(
                steps * self.pulses_per_step
        ):  # 使用self.pulses_per_step计算脉冲
            self.pulse_once(100)
            if dir == "cw":
                self.position += 1
            else:
                self.position -= 1
            self.check_position()

    def pulse_once(self, delay_micros):
        self.pul.value = 1
        time.sleep(delay_micros / 1e6)  # 延时
        self.pul.value = 0
        time.sleep(delay_micros / 1e6)

    def check_position(self):
        positions = {1 / 5: "1/5", 2 / 5: "2/5", 3 / 5: "3/5", 4 / 5: "4/5"}
        for fraction, name in positions.items():
            target_position = fraction * self.steps_per_revolution
            if abs(self.position - target_position) < 2:
                response = input(f"Do you want to stop at {name} position? (yes/no) ")
                if response.lower() == "yes":
                    print(f"Stopping at {name}")
                    return

    def read_sensors(self):
        state_start = "Detected" if self.start_sensor.is_active else "Not Detected"
        state_end = "Detected" if self.end_sensor.is_active else "Not Detected"
        print(f"Start Sensor: {state_start}, End Sensor: {state_end}")


if __name__ == "__main__":
    rail_system = RailSystem(19, 26, 21, 20, 8000, 400)  # 添加每步400脉冲的参数
    try:
        while True:
            target_position = int(input("请输入目标位置（步数）: "))
            rail_system.move_to_position(target_position)
            rail_system.read_sensors()
    except KeyboardInterrupt:
        print("程序被用户中断")
    except ValueError:
        print("请输入有效的数字")
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        rail_system.pul.close()
        rail_system.dir.close()
        rail_system.start_sensor.close()
        rail_system.end_sensor.close()
