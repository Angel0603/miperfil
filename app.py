from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    nombre = "Ángel de Jesús Lara Barrera"
    grado = "9no"
    grupo = "B"
    return nombre + "<br>" + grado + "<br>" + grupo

if __name__ == '__main__':
    app.run(debug=True)