"""
@Project        ：TeaPiController
@File           ：device_service.py
@IDE            ：PyCharm
@Author         ：李延
@Date           ：2024/5/14 下午2:13
@Description    ：
"""

from sqlalchemy.orm import Session

from models.base import DeviceModel
from models.schema import DeviceCreateSchema, DeviceSchema


class DeviceService:
    def __init__(self, db: Session):
        self.db = db

    def save_or_update(self, device_data: DeviceCreateSchema):
        try:
            with self.db as session:
                device = (
                    session.query(DeviceModel).filter_by(id=device_data["id"]).first()
                )
                if device:
                    # Update existing device
                    for key, value in device_data.items():
                        setattr(device, key, value)
                else:
                    # Create a new device
                    device = DeviceSchema(**device_data.model_dump())
                    session.add(device)
                session.commit()
        except Exception as e:
            print(e)
            raise e

    def replace_devices(self, machine_id, devices: list[DeviceCreateSchema]):
        try:
            # 开始一个新的事务
            with self.db.begin() as transaction:
                try:
                    # 删除特定机器的所有现有设备
                    self.db.execute(
                        "LOCK TABLES devices WRITE"  # 根据您的数据库类型，这里的语法可能需要调整
                    )
                    self.db.query(DeviceModel).filter_by(machine_id=machine_id).delete(
                        synchronize_session=False
                    )

                    # 插入新的设备数据
                    for device_data in devices:
                        self.db.add(device_data)

                    # 提交事务以保存更改
                    transaction.commit()
                except:
                    # 如果发生异常，回滚到事务开始前的状态
                    transaction.rollback()
                    raise
        except Exception as e:
            print(e)
            raise e
