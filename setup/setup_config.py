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
        config_dict = config_service.get_config("rabbitmq")
        logger.info(f"config_dict: {config_dict}
        ")