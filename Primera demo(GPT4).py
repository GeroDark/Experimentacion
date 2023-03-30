import openai
import tkinter as tk
from tkinter import messagebox
openai.api_key = "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"


#Estoy en la rama master

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

def submit():
    tipo = tipo_var.get()
    datos = datos_entry.get()
    angulo = angulo_entry.get()
    fuente = fuente_entry.get()
    descargo = descargo_entry.get()
    testimonios = testimonios_entry.get()
    rango_caracteres = rango_caracteres_entry.get()
    contexto = contexto_entry.get()

    resultado = generar_nota_periodistica_2(tipo, datos, angulo, fuente, descargo, testimonios, rango_caracteres,contexto)
    messagebox.showinfo("Resultado", resultado)

root = tk.Tk()
root.title("Generador de Notas Periodísticas")

tipo_label = tk.Label(root, text="Tipo de redacción:")
tipo_label.grid(row=0, column=0, sticky="w")

tipo_var = tk.StringVar(root)
tipo_var.set("Noticia")

tipo_menu = tk.OptionMenu(root, tipo_var, "Noticia", "Reportaje", "Crónica", "Entrevista", "Columna de opinión", "Editorial", "Reseña o Crítica")
tipo_menu.grid(row=0, column=1, sticky="w")

datos_label = tk.Label(root, text="Datos:")
datos_label.grid(row=1, column=0, sticky="w")
datos_entry = tk.Entry(root)
datos_entry.grid(row=1, column=1, sticky="w")

angulo_label = tk.Label(root, text="Ángulo:")
angulo_label.grid(row=2, column=0, sticky="w")
angulo_entry = tk.Entry(root)
angulo_entry.grid(row=2, column=1, sticky="w")

fuente_label = tk.Label(root, text="Fuente:")
fuente_label.grid(row=3, column=0, sticky="w")
fuente_entry = tk.Entry(root)
fuente_entry.grid(row=3, column=1, sticky="w")

descargo_label = tk.Label(root, text="Descargo:")
descargo_label.grid(row=4, column=0, sticky="w")
descargo_entry = tk.Entry(root)
descargo_entry.grid(row=4, column=1, sticky="w")

testimonios_label = tk.Label(root, text="Testimonios:")
testimonios_label.grid(row=5, column=0, sticky="w")
testimonios_entry = tk.Entry(root)
testimonios_entry.grid(row=5, column=1, sticky="w")

rango_caracteres_label = tk.Label(root, text="Rango de caracteres:")
rango_caracteres_label.grid(row=7, column=0, sticky="w")
rango_caracteres_entry = tk.Entry(root)
rango_caracteres_entry.grid(row=7, column=1, sticky="w")
contexto_label = tk.Label(root, text="Contexto:")
contexto_label.grid(row=8, column=0, sticky="w")
contexto_entry = tk.Entry(root)
contexto_entry.grid(row=8, column=1, sticky="w")


submit_button = tk.Button(root, text="Generar nota periodística", command=submit)
submit_button.grid(row=9, column=0, columnspan=2)

root.mainloop()