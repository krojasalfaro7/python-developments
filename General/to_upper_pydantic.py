from typing import Optional
from pydantic import BaseModel, validator


class AddressModel(BaseModel):
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    neighborhood: Optional[str] = None
    pincode: Optional[str] = None
    lat: Optional[str] = None
    long: Optional[str] = None

    @validator("city", pre=True)
    def to_upper(cls, info):
        return info.upper() if info else info

addrs = AddressModel(city="caracas")
print(addrs)
