from flask import Flask, request

# creamos un objeto de clase Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<center><h1>Hola mundo con Flask</h1></center>'

@app.route('/saludo')
def saludo():
    nombre = request.args.get('nombre','')
    return f"<h1>Hola {nombre}</h1>"

@app.route('/sumar/<int:a>/<int:b>')
def sumar(a,b):
    resultado = a + b
    return f"<center><h1>La suma de {a} + {b} es {resultado} </h1></center>"

@app.route('/<operacion>/<int:num1>/<int:num2>')
def operaciones(operacion,num1,num2):
    if operacion=="suma":
        res = num1 + num2
    elif operacion=="resta":
        res= num1 - num2
    elif operacion=="multiplicacion":
        res= num1 * num2
    elif operacion=="division":
        if num2==0:
            return "<h1>Error: División por cero no permitida</h1>"
        res= float(num1 / num2)        
    else:
        return "<h1>Error: Operación no válida</h1>"
        
    return f"<h1>La {operacion} de {num1} y {num2} es {res}</h1>"


app.run(debug=True)