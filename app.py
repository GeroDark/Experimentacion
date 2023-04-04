from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

def generar_nota_periodistica_2(tipo, datos, angulo, fuente, descargo, testimonios, rango_caracteres,contexto):
    response=openai.ChatCompletion.create(
        model="gpt-4",
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.8,
        messages=[
            {"role": "system", "content": "Tu eres un redactor de notas periodisticas"},
            {"role": "user", "content": f"Redacta una {tipo} profesional en un rango de {rango_caracteres} caracteres para un diario serio utilizando la siguiente información:\n\nDatos: {datos}\nAngulo: {angulo}\nFuente: {fuente}\nDescargo: {descargo}\nTestimonios: {testimonios}\n\nTitular:\n{{titulo}}\n\nNota periodística:\n{{contenido}}"},
            
        ]
    )
    return response['choices'][0]['message']['content']

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