from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    设备配置
    """

    VERSION: str = "v1.0"  # 版本
    MACHINE_NAME: str = "init_device"
    MACHINE_IP: str = "192.168.1.114"
    MACHINE_CODE: str = "A01244261712"
    SERVER_API: str = "http://127.0.0.1:8000/api/v1"
    RELOAD: bool = True
    WORKING_CONDITION = False
    # RabbitMq
    RABBITMQ_HOST: str = "101.126.69.153"
    RABBITMQ_PORT: int = 5672
    RABBITMQ_USERNAME: str = "rabbitmq"
    RABBITMQ_PASSWORD: str = "rabbitmq"
    RABBITMQ_VHOST: str = "/"
    RABBITMQ_EXCHANGE: str = "exchange"

    # Server API
    GET_MACHINE_ALL: str = "machine/all/{machine_id}"
    GET_MACHINE_INFO: str = "machine/{machine_id}"
    GET_ORDER_INFO: str = "order/queued/"

    class Config:
        case_sensitive = True  # 区分大小写


# 实例化获取配置类
settings = Settings()
