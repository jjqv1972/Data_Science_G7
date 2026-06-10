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

app.run(debug=True)