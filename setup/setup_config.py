from models.schema import MachineSchema
from seeting import settings
from services.config_service import ConfigService
from services.device_service import DeviceService
from services.http_service import HttpService
from services.machine_service import MachineService
from setup.setup_database import get_db_pro
from utils.log_util import logger


def setup_config():
    # 设置配置文件路径
    with get_db_pro() as db:
        config_service = ConfigService(db)
        config_dict = config_service.get_server_config()
    server_api = next(
        (config.value for config in config_dict if config.key == "servcer_api"), None
    )
    machine_all = next(
        (config.value for config in config_dict if config.key == "get_machine_all"),
        None,
    )
    url = (
        f'{server_api}{machine_all.replace("{machine_id}", f"{settings.MACHINE_CODE}")}'
    )
    http_service = HttpService(url)
    response = http_service.get()
    if response["data"]["code"] != 200:
        logger.error(f"获取配置失败：{response['data']['code']}")
        return
    machine_config = response["data"]["data"]
    machine_data = MachineSchema(
        id=machine_config["id"],
        name=machine_config["name"],
        ip=machine_config.get("raspberry_ip"),
        code=machine_config["machine_code"],
    )
    # try:
    with get_db_pro() as db:
        machine_service = MachineService(db)
        machine_service.save_or_update(machine_data.model_dump())
        device_service = DeviceService(db)
        device_service.replace_devices(machine_data.id, machine_config["devices"])

    # except Exception as e:
    #     logger.error(f"配置保存失败：{e}")
    #     return
