"""
@Project        ：TeaPiController
@File           ：base.py
@IDE            ：PyCharm
@Author         ：李延
@Date           ：2024/5/13 下午4:58
@Description    ：
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.database import Base


class MachineModel(Base):
    """
    Base class for all machine models.
    """

    __tablename__ = "machine"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ip = Column(String)
    code = Column(String)
    devices = relationship("DeviceModel", back_populates="machine")  # 添加这一行


class DeviceModel(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    device_id = Column(Integer, ForeignKey("machine.id"))
    type = Column(Integer)
    status = Column(Integer)
    config = Column(String)  # 这可以是一个JSON字符串
    matter_code = Column(String)
    stock = Column(Integer)
    sort = Column(Integer)
    machine = relationship("MachineModel", back_populates="devices")


class ConfigModel(Base):
    __tablename__ = "config"
    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, nullable=False)
    value = Column(String, nullable=False)
    value_type = Column(String, nullable=False)
    value_group = Column(String, nullable=False)
