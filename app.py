from flask import Flask

app = Flask(__name__)

#criando rota -> endpoint
@app.route('/estagiarios', methods=["GET", "POST"])
def estagiarios():
    return f"Nossa api esta funcionando"

app.run()