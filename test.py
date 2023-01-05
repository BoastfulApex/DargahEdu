import base64


text = "m=630614967066d254af79aa8a;ac.order_id=25;a=100000;c=https/monandapp.uz/;l=uz"

a = text.encode("ascii")

base64_bytes = base64.b64encode(a)
base64_string = base64_bytes.decode("ascii")
url = f"https://checkout.paycom.uz/{base64_string}"
print(url)

click = "service_id=25848&merchant_id=25848&amount=1000&order_id=134&return_url=https://t.me/BoastfulApex8"

c = click.encode("ascii")

base64_bytes = base64.b64encode(c)
base64_string = base64_bytes.decode("ascii")
url = f"https://my.click.uz/services/pay?{base64_string}"
print(url)
