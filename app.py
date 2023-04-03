from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    tipo = data['tipo']
    datos = data['datos']
    angulo = data['angulo']
    fuente = data['fuente']
    descargo = data['descargo']
    testimonios = data['testimonios']
    rango_caracteres = data['rango_caracteres']
    contexto = data['contexto']

    resultado = generar_nota_periodistica_2(tipo, datos, angulo, fuente, descargo, testimonios, rango_caracteres, contexto)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)