from flask import Flask, render_template
import random

app = Flask(__name__)

motivational_quotes = [
    "Claro que hay vida después del estrés postraumático. Claro que hay vida después de ese infierno que has vivido.",
    "Salir adelante requiere tu determinación. Nadie puede tomar por ti la decisión de asumir el control sobre tu propia vida.",
    "Ponte en la primera prioridad de tu vida. Nunca más vuelvas a dar la espalda a ese primer prójimo que eres tú mismo.",
    "Es imprescindible que pongas un punto y final a esa repetición. Aprende a descartar y rechazar las relaciones que no suman.",
    "Confía en la formidable capacidad de tu cerebro para autorrepararse. Esa herida traumática puede ser curada aunque hayan pasado décadas.",
    "La salida del infierno pertenece a aquellos que se autodeterminan y se ponen rápidamente en la tarea de salir adelante.",
    "Tu tarea es tomarte en serio, romper con el ciclo y hacerte invulnerable a que esa situación vuelva a reproducirse.",
    "Aprende a protagonizar tu vida con decisiones que te lleven a elegir aquello que quieres.",
    "Tu energía es valiosa. Deja de dilapidarla en defenderte y úsala para construir un futuro donde no necesites hacerlo.",
    "Rompe con el ciclo vicioso y te harás invulnerable. Esa es la meta y es alcanzable."
]

@app.route('/')
def index():
    page_title = "Proyecto Fénix"
    daily_phrase = random.choice(motivational_quotes)

    return render_template('index.html',
                           title=page_title,
                           phrase=daily_phrase)

if __name__ == '__main__':
    app.run(debug=True)