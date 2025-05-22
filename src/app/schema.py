from typing import Optional

from fastapi import File, UploadFile, Form
from pydantic import BaseModel, EmailStr


class OrderData(BaseModel):
    order_number: str
    email: EmailStr
    first_name: str
    last_name: str
    address: str
    zip: str
    city: str
    country: str
    phone: str
    product_name: str
    product_price: str
    product_image: str = None
    passImage: str = None
    grand_total: str

async def get_order_data(
        first_name: str = Form(...),
        last_name: str = Form(...),
        address: str = Form(...),
        zip: str = Form(...),
        city: str = Form(...),
        country: str = Form(...),
        phone: str = Form(...),
        email: str = Form(...),
        product_name: str = Form(...),
        product_price: str = Form(...),
        grand_total: str = Form(...),
        product_image: Optional[UploadFile] = File(None),
        passImage: Optional[UploadFile] = File(None),
) -> dict:
    return {
        "first_name": first_name,
        "last_name": last_name,
        "address": address,
        "zip": zip,
        "city": city,
        "country": country,
        "phone": phone,
        "email": email,
        "product_name": product_name,
        "product_price": product_price,
        "grand_total": grand_total,
        "product_image": product_image,
        "passImage": passImage,
    }


class AdminContact(BaseModel):
    name: str
    email: EmailStr
    comment: str


class ResponseMessage(BaseModel):
    message: str
