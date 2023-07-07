from pydantic import (BaseModel,conint,constr,UUID4,Field,PositiveFloat,validator)
from typing import Optional
from uuid import uuid4

class PaymentRequestSerializer(BaseModel):
    amount: PositiveFloat
    currency:constr(to_upper=True,strip_whitespace=True)
    receipt: constr() = Field(default=str(uuid4()))
    notes: Optional[dict]

    @validator("amount")
    def amount_to_paise(cls,value):
        value = value*100
        return value

class PaymentResponseSerializer(BaseModel):
    order_id:constr()