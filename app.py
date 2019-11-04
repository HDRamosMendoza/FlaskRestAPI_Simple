from flask import Flask
'''Aplicativo de servidorr'''
app = Flask(__name__)

'''
    Inicializamos el servidor. Si el 
    archivo se esta ejecutando como archivo principal'''

from products import products

''' Testeo. Ruta de prueba '''
@app.route('/ping')
def ping():
    return 'Pong!'

if __name__ == '__main__':
    app.run(debug=True, port=4000)
