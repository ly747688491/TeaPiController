from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    设备配置
    """

    VERSION: str = "v1.0"  # 版本
    MACHINE_NAME: str = "init_device"
    MACHINE_CODE: str = "SD00001"
    RELOAD: bool = True
    WORKING_CONDITION: bool = False

    class Config:
        case_sensitive = True  # 区分大小写


# 实例化获取配置类
settings = Settings()
