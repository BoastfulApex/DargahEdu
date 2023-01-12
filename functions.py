import base64
import requests

def send_sms(otp, phone):
    username = "zoneagency"
    password = "j2e4AEFs84"
    sms_data = {
        "messages":[{"recipient":phone,"message-id":"abc00000002","sms":{"originator": "3700","content": {"text": f"Sizning Dargoh o'quv platformasida ro'yxatdan o'tish kodingiz: {otp}"}}}]}
    url = "http://91.204.239.44/broker-api/send"
    res = requests.post(url=url, headers={}, auth=(username, password), json=sms_data)
    print(res.json)


def get_payme_url(succes_url, user_id):
    text = f"m=63be69bbd3af34dee9995a1d;ac.order_id={user_id};a=100000;c={succes_url}"
    a = text.encode("ascii")
    base64_bytes = base64.b64encode(a)
    base64_string = base64_bytes.decode("ascii")
    url = f"https://checkout.paycom.uz/{base64_string}"
    return url


def get_click_url(service_id, merchant_id, amount, transaction_id, return_url):
    click = f"service_id={service_id}&merchant_id={merchant_id}&amount={amount}&transaction_param={transaction_id}&return_url={return_url}"
    url = f"https://my.click.uz/services/pay?{click}"
    return url