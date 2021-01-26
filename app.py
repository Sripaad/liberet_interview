from math import nan, prod
from flask import Flask
from flask import json
from flask.globals import request
from flask.json import jsonify
from sqlalchemy.ext.declarative.api import as_declarative


liberet_store = [
  {
    "ShoppingCartId": "shop_01",
    "userId": "user_01",
    "orderReference": "order_01",
    "productId": "prod_03",
    "todayIs": "2021-01-06T20:20:08.195Z",
    "serviceDate": "2021-01-020T09:00:00.000Z",
    "serviceSchedule": "9:00-11:00",
    "productName": "Tuna Steak",
    "supplier": "Not a fancy place",
    "deliveryType": "DELIVERY",
    "productCost": 310,
    "deliveryFee": 19,
    "deliveryFeeExplanation": "Schedule order with more than 60$",
    "totalCost": 3793
  },
  {
    "ShoppingCartId": "shop_01",
    "userId": "user_01",
    "orderReference": "order_01",
    "productId": "prod_04",
    "todayIs": "2021-01-06T20:20:08.195Z",
    "serviceDate": "2021-01-020T09:00:00.000Z",
    "serviceSchedule": "9:00-11:00",
    "productName": "Alfredo pasta",
    "supplier": "Not a fancy place",
    "deliveryType": "DELIVERY",
    "productCost": 145,
    "deliveryFee": "",
    "deliveryFeeExplanation": "",
    "totalCost": ""
  },
  {
    "ShoppingCartId": "shop_01",
    "userId": "user_01",
    "orderReference": "order_02",
    "productId": "prod_04",
    "todayIs": "2021-01-06T20:20:08.195Z",
    "serviceDate": "2021-01-020T11:00:00.000Z",
    "serviceSchedule": "11:00-13:00",
    "productName": "Alfredo pasta",
    "supplier": "Not a fancy place",
    "deliveryType": "PICKUP",
    "productCost": 145,
    "deliveryFee": 0,
    "deliveryFeeExplanation": "deliveryType its not DELIVERY",
    "totalCost": ""
  },
  {
    "ShoppingCartId": "shop_01",
    "userId": "user_01",
    "orderReference": "order_02",
    "productId": "prod_03",
    "todayIs": "2021-01-06T20:20:08.195Z",
    "serviceDate": "2021-01-020T11:00:00.000Z",
    "serviceSchedule": "11:00-13:00",
    "productName": "Tuna Steak",
    "supplier": "Not a fancy place",
    "deliveryType": "PICKUP",
    "productCost": 310,
    "deliveryFee": "",
    "deliveryFeeExplanation": "",
    "totalCost": ""
  },
  {
    "ShoppingCartId": "shop_01",
    "userId": "user_01",
    "orderReference": "order_03",
    "productId": "prod_09",
    "todayIs": "2021-01-06T20:20:08.195Z",
    "serviceDate": "2021-01-020T13:00:00.000Z",
    "serviceSchedule": "13:00-15:00",
    "productName": "Mexican tamaliza for 20",
    "supplier": "Still better than brocoli",
    "deliveryType": "DELIVERY",
    "productCost": 2500,
    "deliveryFee": 199,
    "deliveryFeeExplanation": "One of the products in the order cost higher or equal 2000",
    "totalCost": ""
  },
  {
    "ShoppingCartId": "shop_01",
    "userId": "user_01",
    "orderReference": "order_03",
    "productId": "prod_06",
    "todayIs": "2021-01-06T20:20:08.195Z",
    "serviceDate": "2021-01-020T13:00:00.000Z",
    "serviceSchedule": "13:00-15:00",
    "productName": "Mexican Tamal 1 pz",
    "supplier": "Still better than brocoli",
    "deliveryType": "DELIVERY",
    "productCost": 39,
    "deliveryFee": "",
    "deliveryFeeExplanation": "",
    "totalCost": ""
  },
  {
    "ShoppingCartId": "shop_01",
    "userId": "user_01",
    "orderReference": "order_03",
    "productId": "prod_07",
    "todayIs": "2021-01-06T20:20:08.195Z",
    "serviceDate": "2021-01-020T13:00:00.000Z",
    "serviceSchedule": "13:00-15:00",
    "productName": "Banana puddin",
    "supplier": "Still better than brocoli",
    "deliveryType": "DELIVERY",
    "productCost": 29,
    "deliveryFee": "",
    "deliveryFeeExplanation": "",
    "totalCost": ""
  },
  {
    "ShoppingCartId": "shop_01",
    "userId": "user_01",
    "orderReference": "order_03",
    "productId": "prod_08",
    "todayIs": "2021-01-06T20:20:08.195Z",
    "serviceDate": "2021-01-020T13:00:00.000Z",
    "serviceSchedule": "13:00-15:00",
    "productName": "Black beans",
    "supplier": "Still better than brocoli",
    "deliveryType": "DELIVERY",
    "productCost": 30,
    "deliveryFee": "",
    "deliveryFeeExplanation": "",
    "totalCost": ""
  },
  {
    "ShoppingCartId": "shop_01",
    "userId": "user_01",
    "orderReference": "order_04",
    "productId": "prod_06",
    "todayIs": "2021-01-06T20:20:08.195Z",
    "serviceDate": "2021-01-020T13:00:00.000Z",
    "serviceSchedule": "9:00-11:00",
    "productName": "Mexican Tamal 1 pz",
    "supplier": "Still better than brocoli",
    "deliveryType": "DELIVERY",
    "productCost": 39,
    "deliveryFee": 28,
    "deliveryFeeExplanation": "Schedule order with less than 60$",
    "totalCost": ""
  },
  {
    "ShoppingCartId": "shop_02",
    "userId": "user_02",
    "orderReference": "order_05",
    "productId": "prod_03",
    "todayIs": "2021-01-020T08:00:00.000Z",
    "serviceDate": "2021-01-020T09:00:00.000Z",
    "serviceSchedule": "9:00-11:00",
    "productName": "Tuna Steak",
    "supplier": "Not a fancy place",
    "deliveryType": "DELIVERY",
    "productCost": 310,
    "deliveryFee": 28,
    "deliveryFeeExplanation": "Express order with more than 60$",
    "totalCost": 3812
  },
  {
    "ShoppingCartId": "shop_02",
    "userId": "user_02",
    "orderReference": "order_05",
    "productId": "prod_04",
    "todayIs": "2021-01-020T08:00:00.000Z",
    "serviceDate": "2021-01-020T09:00:00.000Z",
    "serviceSchedule": "9:00-11:00",
    "productName": "Alfredo pasta",
    "supplier": "Not a fancy place",
    "deliveryType": "DELIVERY",
    "productCost": 145,
    "deliveryFee": "",
    "deliveryFeeExplanation": "",
    "totalCost": ""
  },
  {
    "ShoppingCartId": "shop_02",
    "userId": "user_02",
    "orderReference": "order_06",
    "productId": "prod_04",
    "todayIs": "2021-01-020T08:00:00.000Z",
    "serviceDate": "2021-01-020T11:00:00.000Z",
    "serviceSchedule": "9:00-11:00",
    "productName": "Alfredo pasta",
    "supplier": "Not a fancy place",
    "deliveryType": "RESERVATION",
    "productCost": 145,
    "deliveryFee": 0,
    "deliveryFeeExplanation": "deliveryType its not DELIVERY",
    "totalCost": ""
  },
  {
    "ShoppingCartId": "shop_02",
    "userId": "user_02",
    "orderReference": "order_06",
    "productId": "prod_03",
    "todayIs": "2021-01-020T08:00:00.000Z",
    "serviceDate": "2021-01-020T11:00:00.000Z",
    "serviceSchedule": "9:00-11:00",
    "productName": "Tuna Steak",
    "supplier": "Not a fancy place",
    "deliveryType": "RESERVATION",
    "productCost": 310,
    "deliveryFee": "",
    "deliveryFeeExplanation": "",
    "totalCost": ""
  },
  {
    "ShoppingCartId": "shop_02",
    "userId": "user_02",
    "orderReference": "order_07",
    "productId": "prod_09",
    "todayIs": "2021-01-020T11:00:00.000Z",
    "serviceDate": "2021-01-020T13:00:00.000Z",
    "serviceSchedule": "9:00-11:00",
    "productName": "Mexican tamaliza for 20",
    "supplier": "Still better than brocoli",
    "deliveryType": "DELIVERY",
    "productCost": 2500,
    "deliveryFee": 199,
    "deliveryFeeExplanation": "One of the products in the order cost higher or equal 2000",
    "totalCost": ""
  },
  {
    "ShoppingCartId": "shop_02",
    "userId": "user_02",
    "orderReference": "order_07",
    "productId": "prod_06",
    "todayIs": "2021-01-020T11:00:00.000Z",
    "serviceDate": "2021-01-020T13:00:00.000Z",
    "serviceSchedule": "9:00-11:00",
    "productName": "Mexican Tamal 1 pz",
    "supplier": "Still better than brocoli",
    "deliveryType": "DELIVERY",
    "productCost": 39,
    "deliveryFee": "",
    "deliveryFeeExplanation": "",
    "totalCost": ""
  },
  {
    "ShoppingCartId": "shop_02",
    "userId": "user_02",
    "orderReference": "order_07",
    "productId": "prod_07",
    "todayIs": "2021-01-020T11:00:00.000Z",
    "serviceDate": "2021-01-020T13:00:00.000Z",
    "serviceSchedule": "9:00-11:00",
    "productName": "Banana puddin",
    "supplier": "Still better than brocoli",
    "deliveryType": "DELIVERY",
    "productCost": 29,
    "deliveryFee": "",
    "deliveryFeeExplanation": "",
    "totalCost": ""
  },
  {
    "ShoppingCartId": "shop_02",
    "userId": "user_02",
    "orderReference": "order_07",
    "productId": "prod_08",
    "todayIs": "2021-01-020T11:00:00.000Z",
    "serviceDate": "2021-01-020T13:00:00.000Z",
    "serviceSchedule": "9:00-11:00",
    "productName": "Black beans",
    "supplier": "Still better than brocoli",
    "deliveryType": "DELIVERY",
    "productCost": 30,
    "deliveryFee": "",
    "deliveryFeeExplanation": "",
    "totalCost": ""
  },
  {
    "ShoppingCartId": "shop_02",
    "userId": "user_02",
    "orderReference": "order_08",
    "productId": "prod_06",
    "todayIs": "2021-01-020T11:00:00.000Z",
    "serviceDate": "2021-01-020T13:00:00.000Z",
    "serviceSchedule": "9:00-11:00",
    "productName": "Mexican Tamal 1 pz",
    "supplier": "Still better than brocoli",
    "deliveryType": "DELIVERY",
    "productCost": 39,
    "deliveryFee": 38,
    "deliveryFeeExplanation": "Express order with less than 60$",
    "totalCost": ""
  }
]


app = Flask(__name__)

def get_order_dict(userId):
    orderDeliveryFee, orderCost, totalDeliveryFee, totalOrderCost, totalCost = 0, 0, 0.0, 0.0, 0.0
  
    for store in liberet_store:
      if userId == store["userId"]:
        orderId = str(store["orderReference"])
        productId = str(store["productId"])
        productPrice = store["productCost"]
        amount = store["deliveryFee"]
        products = [productId, amount, productPrice]
        orderCost = productPrice + amount
        orderDeliveryFee += amount
        orders = [orderId, products, orderCost, orderDeliveryFee]
        totalDeliveryFee += orderDeliveryFee
        totalOrderCost += orderCost
        totalCost += totalDeliveryFee + totalCost
        return jsonify(orders, totalDeliveryFee, totalOrderCost, totalCost)

def get_order_val():
    return jsonify({'orderReference' : 'order_8'})

@app.route("/", methods = ["GET"])
def test():
    return {
        'test' : 'testSuccessful'
    }

@app.route("/shoppingCart/<string:userId>", methods = ["GET"])
def get_shoppingCart(userId):
    for store in liberet_store:
        if store["userId"] == userId:
            orderdict = get_order_dict(userId)
            try: 
                return orderdict
            except:    
                return jsonify({"message": "Order does not exist"})

@app.route("/shoppingCart/<string:userId>/complete", methods = ['POST'])
def complete_shoppingCart(userId):
    if request.method == 'POST':
        return jsonify({userId : "Cart is complete"}), 204

@app.route("/shoppingCart/<string:userId>/remove/<string:orderId>/<string:productId>", methods = ["DELETE"])
def del_shoppingCart(userId, orderId, productId):
    if request.method == 'DELETE':
        for store in liberet_store:
            if store["userId"] == userId and store["orderReference"] == orderId and store["productId"] == productId:
                store["productId"] = None
        try: 
            return '', 204 
        except:    
            return jsonify({"message": "Order does not exist"})

@app.route("/shoppingCart/<string:userId>/add", methods = ["POST"])
def add_product(userId):
    if request.method == 'POST':
      req_data = request.get_json(force=True)
      for store in liberet_store:
        if req_data['orderReference'] == "None":
          orderReference = get_order_val()
          new_store = {
          'userId' : userId,
          'orderReference' : orderReference,
          'productId' : req_data['productId'],
          'amount' : req_data['amount'],
          'serviceDate' : req_data['serviceDate'],
          'serviceSchedule' : req_data['serviceSchedule'],
          'supplier' : req_data['supplier'],
          'deliveryType' : req_data['deliveryType'],
          'productCost' : req_data['productCost'],
          }
          store.append(new_store)
          return jsonify(orderReference)
        else:
          orderReference = req_data['orderReference']
          new_store = {
          'userId' :userId,
          'orderReference' : orderReference,
          'productId' : req_data['productId'],
          'amount' : req_data['amount'],
          'serviceDate' : req_data['serviceDate'],
          'serviceSchedule' : req_data['serviceSchedule'],
          'supplier' : req_data['supplier'],
          'deliveryType' : req_data['deliveryType'],
          'productCost' : req_data['productCost'],
          }
          store.append(new_store)
          return jsonify(orderReference)

    



if __name__ == "__main__":
    app.run(debug=True, port= 6574)