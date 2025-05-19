from email.message import EmailMessage
import aiosmtplib
import os

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

async def send_email(subject: str, recipient: str, html_content: str):
    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content("This is an HTML email. Please view it in an HTML compatible email client.")
    msg.add_alternative(html_content, subtype="html")

    await aiosmtplib.send(
        msg,
        hostname="smtp.gmail.com",
        port=465,
        username=EMAIL_ADDRESS,
        password=EMAIL_PASSWORD,
        use_tls=True,
    )
