from sqlalchemy.orm import Session

from models.base import ConfigModel
from models.schema import ConfigBaseSchema


class ConfigService:
    def __init__(self, db: Session):
        self.db = db

    def get_config(self, config_group: str):
        """
        获取后台服务配置信息
        """
        try:
            with self.db as session:
                server_config = (
                    session.query(ConfigModel)
                    .filter(ConfigModel.value_group == config_group)
                    .all()
                )
                server_dict = [
                    ConfigBaseSchema.model_validate(config) for config in server_config
                ]
                return server_dict
        except Exception as e:
            print(e)
            return None
