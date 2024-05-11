from typing import List

from gpiozero import OutputDevice


def ctrl_motor_clean(GPIO_list: List[int]):
    """
    Control the motor to clean the dishes.
    :param ssid_list: List of SSIDs of the dishes.
    :return: None
    """

    for GPIO_ in GPIO_list:
        motor = OutputDevice(GPIO_)
        motor.on()


def stop_motor_clean(GPIO_list: List[int]):
    """
    Stop the motor.
    :param GPIO_list: List of GPIOs of the motors.
    :return: None
    """
    for GPIO_ in GPIO_list:
        motor = OutputDevice(GPIO_)
        motor.off()
