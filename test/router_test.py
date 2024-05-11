"""
@Project        ：TeaPiController 
@File           ：router_test.py
@IDE            ：PyCharm 
@Author         ：李延
@Date           ：2024/5/6 下午2:15 
@Description    ：
"""
from controllers.router import init_router

if __name__ == "__main__":
    try:
        while True:
            gpio_list = []
            action = input("请输入要执行的操作：")
            while True:
                gpio = input("请输入执行操作的设备（输入 'done' 结束输入）：")
                if gpio.lower() == "done":
                    break
                try:
                    # 将输入转换为整数并添加到列表中
                    gpio_list.append(int(gpio))
                except ValueError:
                    print("请输入有效的数字！")
            # 创建 JSON 字符串
            operation_data = {"action": action, "GPIO_list": gpio_list}
            init_router(ch="", method="", properties="", body=str(operation_data))
    except Exception as e:
        print(e)
