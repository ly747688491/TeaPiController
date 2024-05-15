from sqlalchemy.orm import Session

from models.base import Config
from models.schema import ConfigBase
from setup.setup_database import get_db


class ConfigService:
    def __init__(self, db: Session):
        self.db = db

    def get_server_config(self):
        """
        获取后台服务配置信息
        """
        try:
            with self.db as session:
                server_config = (
                    session.query(Config).filter(Config.value_group == "server").all()
                )
                server_dict = [
                    ConfigBase.model_validate(config) for config in server_config
                ]
                return server_dict
        except Exception as e:
            print(e)
            return None
