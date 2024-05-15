"""
@Project        ：TeaPiController
@File           ：machine_service.py
@IDE            ：PyCharm
@Author         ：李延
@Date           ：2024/5/14 下午2:08
@Description    ：
"""

from sqlalchemy.orm import Session

from models.base import MachineModel
from models.schema import MachineCreateSchema


class MachineService:
    def __init__(self, db: Session):
        self.db = db

    def save_or_update(self, machine_data: MachineCreateSchema):
        try:
            with self.db as session:
                machine = (
                    session.query(MachineModel).filter_by(code=machine_data["code"]).first()
                )
                if machine:
                    for key, value in machine_data.items():
                        setattr(machine, key, value)
                else:
                    session.add(machine_data)
                session.commit()
        except Exception as e:
            raise e
