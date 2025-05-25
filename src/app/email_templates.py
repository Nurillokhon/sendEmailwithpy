# Email uchun HTML templatelar

admin_template = """
<div style="max-width: 600px; margin: auto; background-color: #fff; border: 1px solid #ccc; padding: 20px;">
  <h2 style="text-align: center; border-bottom: 1px dashed #ccc; padding-bottom: 10px;">🧾 Chek / Invoice (Admin uchun)</h2>
  <p><b>Buyurtma raqami:</b> {{order_number}}</p>
  <hr style="border-top: 1px dashed #ccc;">
  <h3>👤 Mijoz Ma'lumotlari</h3>
  <p><b>Ism:</b> {{first_name}}</p>
  <p><b>Familiya:</b> {{last_name}}</p>
  <p><b>Manzil:</b> {{address}}</p>
  <p><b>ZIP:</b> {{zip}}</p>
  <p><b>Shahar:</b> {{city}}</p>
  <p><b>Davlat:</b> {{country}}</p>
  <p><b>Telefon:</b> {{phone}}</p>
  <p><b>Email:</b> {{email}}</p>
  <hr style="border-top: 1px dashed #ccc;">
  <h3>📦 Mahsulotlar</h3>
  <p><b>Nomi:</b> {{product_name}}</p>
  <p><b>Narxi:</b> {{product_price}}</p>
  <hr style="border-top: 1px dashed #ccc;">
  <img src="https://api.solosimcard.com/{{product_image}}" alt="Mahsulot rasmi" style="max-width: 300px;">
  <img src="https://api.solosimcard.com/{{passImage}}" alt="Pass Image" style="max-width: 300px;">
  <hr style="border-top: 1px dashed #ccc;">
  <h2 style="text-align: right; color: #000;">💰 Umumiy narx: <span style="color: #007BFF;">{{grand_total}}</span></h2>
  <p style="text-align: center; font-size: 12px; color: #888; margin-top: 30px;">Rahmat! Sizning buyurtmangiz tez orada yetkaziladi.</p>
</div>
"""

user_template = """
<div style="max-width: 600px; margin: auto; background-color: #fff; border: 1px solid #ccc; padding: 20px;">
  <h2 style="text-align: center; border-bottom: 1px dashed #ccc; padding-bottom: 10px;">🧾 Chek / Invoice (User uchun)</h2>
  <p><b>Buyurtma raqami:</b> {{order_number}}</p>
  <hr style="border-top: 1px dashed #ccc;">
  <h3>👤 Mijoz Ma'lumotlari</h3>
  <p><b>Ism:</b> {{first_name}}</p>
  <p><b>Familiya:</b> {{last_name}}</p>
  <p><b>Manzil:</b> {{address}}</p>
  <p><b>ZIP:</b> {{zip}}</p>
  <p><b>Shahar:</b> {{city}}</p>
  <p><b>Davlat:</b> {{country}}</p>
  <p><b>Telefon:</b> {{phone}}</p>
  <p><b>Email:</b> {{email}}</p>
  <hr style="border-top: 1px dashed #ccc;">
  <h3>📦 Mahsulotlar</h3>
  <p><b>Nomi:</b> {{product_name}}</p>
  <p><b>Narxi:</b> {{product_price}}</p>
  <p><b>Tavsif:</b> {{product_describ}}</p>
  <hr style="border-top: 1px dashed #ccc;">
  <p>To'lov Bank Transfer orqali amalga oshiriladi. Iltimos, chekni saqlang.</p>
  <p>Bank : 토스뱅크 (ToSS Bank)</p>
  <p>Hisob raqam: 1001-3322-9177</p>
  <p>Hisob raqam egasi: Akhmadkulov</p>
  <hr style="border-top: 1px dashed #ccc;">
  <h2 style="text-align: right; color: #000;">💰 Umumiy narx: <span style="color: #007BFF;">{{grand_total}}</span></h2>
  <p style="text-align: center; font-size: 12px; color: #888; margin-top: 30px;">Rahmat! Sizning buyurtmangiz tez orada yetkaziladi.</p>
</div>
"""


admin_contact_template = """
<html>
<body>
    <h2>Yangi aloqa xabari</h2>
    <p><strong>Ism:</strong> {{name}}</p>
    <p><strong>Email:</strong> {{email}}</p>
    <p><strong>Xabar:</strong></p>
    <p>{{comment}}</p>
</body>
</html>
"""

def render_template(template: str, data: dict) -> str:
    for key, value in data.items():
        if value is None:
            value = ""
        template = template.replace(f"{{{{{key}}}}}", str(value))
    return template
