from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, IPvAnyAddress
from pydantic.alias_generators import to_camel


class DeviceBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Optional[str] = Field(
        ..., example="Sensor", description="The name of the device"
    )
    device_id: Optional[int] = Field(None, description="The associated machine's ID")
    type: Optional[int] = Field(..., description="The type code of the device")
    status: Optional[int] = Field(
        ..., description="The current status code of the device"
    )
    config: Optional[str] = Field(
        None, description="JSON string with the device configuration"
    )
    matter_code: Optional[str] = Field(
        None, description="The matter code of the device"
    )
    stock: Optional[int] = Field(
        None, ge=0, description="The stock count of the device"
    )
    sort: Optional[int] = Field(None, description="The sorting index of the device")


class DeviceCreate(DeviceBase):
    pass


class Device(DeviceBase):
    id: Optional[int] = Field(..., description="The unique ID of the device")


class MachineBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Optional[str] = Field(
        ..., example="Machine A", description="The name of the machine"
    )
    ip: Optional[IPvAnyAddress] = Field(
        None, description="The IP address of the machine"
    )
    code: Optional[str] = Field(None, description="The unique code of the machine")


class MachineCreate(MachineBase):
    pass


class Machine(MachineBase):
    id: Optional[int] = Field(..., description="The unique ID of the machine")
    components: List[Device] = []


class ConfigBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    key: Optional[str] = Field(None, description="The key of the configuration")
    value: Optional[str] = Field(None, description="The value of the configuration")
    value_type: str
    value_group: str


class ConfigCreate(ConfigBase):
    pass


class Config(ConfigBase):
    id: Optional[int]
