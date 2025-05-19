import ssl
from email.message import EmailMessage
from typing import Union

import aiosmtplib
import certifi
from pydantic import EmailStr

from config.settings import EMAIL_ADDRESS, EMAIL_PASSWORD

print("EMAIL_ADDRESS", EMAIL_ADDRESS)


async def send_email(subject: str, recipient: Union[EmailStr, str], html_content: str):
    if not recipient:
        raise ValueError("Email oluvchi manzil ko'rsatilmagan")

    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content("This is an HTML email. Please view it in an HTML compatible email client.")
    msg.add_alternative(html_content, subtype="html")

    ssl_context = ssl.create_default_context(cafile=certifi.where())

    print("Sending email...", msg)

    await aiosmtplib.send(
        msg,
        hostname="smtp.gmail.com",
        port=465,
        username=EMAIL_ADDRESS,
        password=EMAIL_PASSWORD,
        use_tls=True,
        tls_context=ssl_context
    )
