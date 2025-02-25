from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Clave de API de OpenAI (asegúrate de usar tu propia clave)
openai.api_key = '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'  # Reemplaza con tu clave de API de OpenAI

# Función para generar la receta usando OpenAI (modelo de chat)
def generar_receta(ingredientes):
    prompt = f"Con los siguientes ingredientes, crea una receta facil, detallando nombre y el paso a paso usando 100 tokens: {ingredientes}"

    # Crear el mensaje de chat
    messages = [
        {"role": "system", "content": "Eres un asistente de cocina."},
        {"role": "user", "content": prompt}
    ]

    try:
        # Solicitar a OpenAI GPT-3.5 o GPT-4 utilizando el endpoint de chat
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Puedes usar "gpt-4" si tienes acceso a GPT-4
            messages=messages,
            max_tokens=120,  # Limitar la respuesta a 60 tokens
            temperature=0.7
        )
        receta = response['choices'][0]['message']['content'].strip()
        return receta
    except Exception as e:
        return f"Error al generar la receta: {e}"

# Ruta principal de la aplicación
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ingredientes = request.form["ingredientes"]
        receta = generar_receta(ingredientes)
        return render_template("index.html", receta=receta)
    return render_template("index.html", receta=None)

if __name__ == "__main__":
    app.run(debug=True)
