from seeting import settings


def setup_config():
    # 设置配置文件路径
    info_url = f"{settings.SERVER_API}//machine/all/{settings.MACHINE_CODE}"
