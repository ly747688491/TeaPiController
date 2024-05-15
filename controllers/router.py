import json

from utils.log_util import logger


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
        pass
        # ctrl_motor_clean(GPIO_list)
    elif action == "end_cleaning":
        pass
        # stop_motor_clean(GPIO_list)
