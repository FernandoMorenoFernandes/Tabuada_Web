from flask import Flask, request, render_template
from datetime import datetime

ano_atual = datetime.now().year


app = Flask(__name__)

@app.route('/')
def index():
#Ao renderizar o template HTML, a variável current_year passa como um argumento para o template:
    return render_template('index.html', ano_atual=ano_atual)

@app.route('/tabuada', methods=['POST'])
def tabuada():
    num = int(request.form['numero'])
    tabuada = [(num, i, num * i) for i in range(1, 11)]
    return render_template('tabuada.html', num=num, tabuada=tabuada, ano_atual=ano_atual)

if __name__ == '__main__':
    app.run(debug=True)

