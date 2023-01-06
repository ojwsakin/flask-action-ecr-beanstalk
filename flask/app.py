from flask import Flask, Response, render_template
import boto3
from functools import wraps
import json
import os
import random
app = Flask(__name__)

def as_json(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        res = f(*args, **kwargs)
        res = json.dumps(res, ensure_ascii=False).encode('utf8')
        return Response(res, content_type='application/json; charset=utf-8')
    return decorated_function

@app.route('/')
def hellohtml():
    return render_template("hello.html")


@app.route('/kospi')
#@as_json
def choice_kospi():
    dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2', aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], aws_secret_access_key=os.environ['AWS_SECRET_KEY'])
    table = dynamodb.Table('stock')
    choice = random.randrange(1, 1900)
    #choice = 1
    kospidata = table.get_item(Key={"id": "%d" %(choice)})
    resultDataCom = kospidata['Item']['company']
    resultDataPrice = kospidata['Item']['price']
    resultDataMarket = kospidata['Item']['market']
    return render_template("kospi.html", resultDataCom=resultDataCom, resultDataPrice=resultDataPrice, resultDataMarket=resultDataMarket)
    #return kospidata['Item']


