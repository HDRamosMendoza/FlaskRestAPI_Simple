from flask import Flask, jsonify, request
''' 
    - jsonify. Nos permite convertir un objeto a un json.
    - request. Proporciona los datos que se enviar por http.
'''
'''Aplicativo de servidorr'''
app = Flask(__name__)
'''
    Inicializamos el servidor. Si el 
    archivo se esta ejecutando como archivo principal
'''
from products import products

''' Testeo. Ruta de prueba - string '''
@app.route('/ping')
def ping():
    return 'Pong!'

''' Testeo: JSON '''
@app.route('/demo_json')
def demo():
    return jsonify({"messsage": "pong!!"})

''' Por defecto se trabaja con method=['GET'] '''
@app.route('/product')
def getProduct():
    return jsonify(products)

@app.route('/products')
def getProducts():
    return jsonify({"products": products})

@app.route('/productsList')
def getProductsList():
    return jsonify({"products": products, "message": "Product's List"})

@app.route('/productsList/<string:product_name>')
def getProductName(product_name):
    print(product_name)
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"Product": productsFound[0]})
    return jsonify({"message": "Product not found"})

@app.route('/products', methods=['POST'])
def addProduct():
    '''
    JSON DE DEMO DEL LADO DEL CLIENTE(INSOMNIA)
    {
        "name": "mouse gaming",
        "price": 45.99,
        "quantity": 2
    }
    '''
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({
        "message": "Product Added Succesfully",
        "products": products
        })

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if(len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Product Updated",
            "product": productFound[0]
        })
    return jsonify({"message": "Product not found"})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            "message": "Product Deleted",
            "products": products
        })
    return jsonify({"message": "Product Not found"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)