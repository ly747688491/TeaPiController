"""
@Project        ：TeaPiController 
@File           ：slide_rail_test.py
@IDE            ：PyCharm 
@Author         ：李延
@Date           ：2024/5/6 下午2:14 
@Description    ：
"""
import time

from gpiozero import OutputDevice, PWMOutputDevice


def define_pins():
    # 注意：确保这里使用的是正确的GPIO引脚编号
    pul = PWMOutputDevice(13, frequency=1000)  # PUL+
    dir_ = OutputDevice(6)  # DIR+

    return pul, dir_


# 定义引脚
pul, dir_ = define_pins()


def rotate_motor(steps, dir):
    # 设置方向
    if dir == "cw":
        dir_.on()
    else:
        dir_.off()

    print(f"Motor direction is now {'CW' if dir_.is_active else 'CCW'}.")

    # 生成脉冲信号
    for _ in range(steps * 400):
        pulse_once(100)


def pulse_once(delay_micros):
    pul.value = 1
    time.sleep(delay_micros / 1e6)  # 延时
    pul.value = 0
    time.sleep(delay_micros / 1e6)


if __name__ == "__main__":
    try:
        while True:
            steps = input("请输入步进步数: ")
            direction = input("请输入运动方向 ('cw' 或 'ccw'): ")
            steps = int(steps)
            rotate_motor(steps, direction)
    except KeyboardInterrupt:
        print("程序被用户中断")
    except ValueError:
        print("请输入有效的数字")
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        pul.close()  # 清理GPIO资源
        dir_.close()
