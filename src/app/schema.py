from pydantic import BaseModel, EmailStr


class OrderData(BaseModel):
    order_number: str
    first_name: str
    last_name: str
    address: str
    zip: str
    city: str
    country: str
    phone: str
    email: EmailStr
    product_name: str
    product_price: str
    product_describ: str = None
    product_image: str = None
    passImage: str = None
    grand_total: str


class AdminContact(BaseModel):
    name: str
    email: EmailStr
    comment: str


class ResponseMessage(BaseModel):
    message: str
