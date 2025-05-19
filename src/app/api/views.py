from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from app.email_templates import admin_template, user_template, render_template, admin_contact_template
from app.email_utils import send_email
from app.utils import generate_order_number
from config.settings import ADMIN_EMAIL
from ..schema import OrderData, AdminContact, ResponseMessage

app = APIRouter(
    tags=["email"],
    responses={404: {"description": "Not found"}},
)


@app.post("/send-invoice", response_model=ResponseMessage, status_code=status.HTTP_201_CREATED)
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
        print(user_email_html)
        await send_email(
            subject=f"Sizning buyurtmangiz: {order.order_number}",
            recipient=order.email,
            html_content=user_email_html,
        )

        return {"message": "Admin va Userga email yuborildi"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Xatolik: {str(e)}")


@app.post("/contact-admin", response_model=ResponseMessage, status_code=status.HTTP_200_OK)
async def contact_admin(data: AdminContact):
    try:
        email_html = render_template(admin_contact_template, data.dict())

        await send_email(
            subject="Yangi aloqa xabari",
            recipient=ADMIN_EMAIL,
            html_content=email_html,
        )

        return {"message": "Xabar admin emailiga yuborildi"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Xatolik: {str(e)}")
