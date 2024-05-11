import json

from utils.log_util import logger

from controllers.motro import ctrl_motor_clean, stop_motor_clean


def init_router(ch, method, properties, body):
    logger.info(f"Received message: {body.decode()}")
    print(f"{ch}")
    print(f"{method}")

    # 解析JSON数据
    message = json.loads(body.decode())
    action = message.get("action")
    GPIO_list = message.get("GPIO_list", [])

    # 根据工作类型参数调用相应的函数
    if action == "start_cleaning":
        ctrl_motor_clean(GPIO_list)
    elif action == "end_cleaning":
        stop_motor_clean(GPIO_list)
