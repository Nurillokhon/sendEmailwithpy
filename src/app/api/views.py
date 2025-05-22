import os.path

from fastapi import APIRouter

from app.email_templates import admin_contact_template
from ..schema import AdminContact

app = APIRouter(
    tags=["email"],
    responses={404: {"description": "Not found"}},
)

from fastapi import APIRouter, HTTPException, status, Depends
from app.email_templates import admin_template, user_template, render_template
from app.email_utils import send_email
from app.utils import generate_order_number
from config.settings import ADMIN_EMAIL, BASE_DIR
from ..schema import OrderData, ResponseMessage, get_order_data

app = APIRouter(
    tags=["email"],
    responses={404: {"description": "Not found"}},
)


@app.post("/send-invoice", response_model=ResponseMessage)
async def send_invoice(data: dict = Depends(get_order_data)):
    try:
        base_dir = f"{BASE_DIR.parent}/media"
        os.makedirs(base_dir, exist_ok=True)
        if data["product_image"]:
            product_image_url = f"{base_dir}/{data['product_image'].filename}"
            with open(product_image_url, "wb", ) as f:
                f.write(await data["product_image"].read())

        if data["passImage"]:
            pass_image_url = f"{base_dir}/{data['passImage'].filename}"
            with open(pass_image_url, "wb") as f:
                f.write(await data["passImage"].read())

        product_image_url = "media/" + data["product_image"].filename
        pass_image_url = "media/" + data["passImage"].filename

        # Generate order number
        order_number = generate_order_number()

        # Create OrderData instance manually
        order = OrderData(
            order_number=order_number,
            first_name=data["first_name"],
            last_name=data["last_name"],
            address=data["address"],
            zip=data["zip"],
            city=data["city"],
            country=data["country"],
            phone=data["phone"],
            email=data["email"],
            product_name=data["product_name"],
            product_price=data["product_price"],
            product_image=product_image_url,
            passImage=pass_image_url,
            grand_total=data["grand_total"],
        )

        # Render and send emails
        data_dict = order.dict()
        admin_email_html = render_template(admin_template, data_dict)
        await send_email(
            subject=f"Yangi buyurtma: {order_number}",
            recipient=ADMIN_EMAIL,
            html_content=admin_email_html,
        )

        user_email_html = render_template(user_template, data_dict)
        await send_email(
            subject=f"Sizning buyurtmangiz: {order_number}",
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
