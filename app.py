from flask import Flask, render_template, request, redirect
from model import Pre_Processamento

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        arquivo = request.form['arq']
        dados = Pre_Processamento(arquivo)
        dados.getArquivo()
        dados.getTxt_limpo()
        dados.getTxt_dividir()
        dados.getRemove_palavras()
        return (f'Abaixo o texto:<br><br>{dados.getRaiz_verbo()}<br><br><h4>Recarregue a página para continuar :)</h4>')
    return render_template('home.html')

@app.route('/info')
def info():
    return render_template('info.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    