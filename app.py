from distutils.debug import DEBUG 
from flask import Flask, render_template#importou render_template

app = Flask(__name__)

#criando rota -> endpoint
#flask é um microframework pq ele n tem padrao de estrutura
@app.route('/')
def home():
    return f"Nossa api esta funcionando"





# @app.route('/estagiarios')
# def estagiarios():
#     return f"JSON estagiarios"

# @app.route('/produtos') #vai exibir os produtos
# def produtos():
#     produtos = ['Pano de prato', 'Croche', 'Toalha', 'Camiseta']
#     return render_template('produtos/listar_produtos.html', produtos=produtos) #recebe o nome do html, para renderizar

app.run(debug=True) 