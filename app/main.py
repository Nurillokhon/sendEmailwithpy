from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from dotenv import load_dotenv
import os

# .env faylni to‘g‘ri yo‘l bilan yuklash
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))


from app.email_templates import admin_template, user_template, render_template
from app.email_utils import send_email
from app.utils import generate_order_number


load_dotenv()

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")

app = FastAPI()

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

@app.post("/send-invoice")
async def send_invoice(order: OrderData):
    try:
        data_dict = order.dict()
        data_dict["order_number"] = generate_order_number()

        # Admin uchun email tayyorlash
        admin_email_html = render_template(admin_template, data_dict)
        await send_email(
            subject=f"Yangi buyurtma: {order.order_number}",
            recipient=ADMIN_EMAIL,
            html_content=admin_email_html,
        )

        # User uchun email tayyorlash
        user_email_html = render_template(user_template, data_dict)
        await send_email(
            subject=f"Sizning buyurtmangiz: {order.order_number}",
            recipient=order.email,
            html_content=user_email_html,
        )

        return {"message": "Admin va Userga email yuborildi"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Xatolik: {str(e)}")

