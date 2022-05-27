from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calc', methods=['POST', 'GET'])
def calc():
    n1 = int(request.form['n1'])

    if 'n2' in request.form:
        n2 = int(request.form['n2'])
    else:
        n2 = 0

    operation = request.form['operation']

    if operation == 'potencia':
        resultado = math.pow(n1, n2)
    elif operation == 'raiz_quadrada':
        resultado = math.sqrt(n1)
    elif operation == 'logaritmo':
        resultado = math.log10(n1)

    return str(resultado)


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)