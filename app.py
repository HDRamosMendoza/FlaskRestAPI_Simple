from flask import Flask, jsonify

''' 
    jsonify. Nos permite convertir
    un objeto a un json
'''

'''Aplicativo de servidorr'''
app = Flask(__name__)

'''
    Inicializamos el servidor. Si el 
    archivo se esta ejecutando como archivo principal'''

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

'''
@app.route('/product', methods=['POST'])
def addProduct():
'''
    
if __name__ == '__main__':
    app.run(debug=True, port=4000)