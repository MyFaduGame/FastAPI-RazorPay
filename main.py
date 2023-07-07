from fastapi import FastAPI
import razorpay
from serializer import (PaymentRequestSerializer,PaymentResponseSerializer)

app = FastAPI()

razor_pay_secret_key='<YOUR_API_KEY>'
razor_pay_secret_key_id='<YOUR_API_SECRET>'


@app.post("/")
def root(request:PaymentRequestSerializer):
    client = razorpay.Client(auth=(razor_pay_secret_key_id,razor_pay_secret_key))
    order = client.order.create(data=request.__dict__)
    order_data = PaymentResponseSerializer(order_id=order['id'])
    return order_data