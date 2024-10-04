from flask import Flask, jsonify, request
from data_generator import generate_credit_data

app = Flask(__name__)

# Rota para gerar múltiplos dados falsos
@app.route('/generate-data', methods=['GET'])
def get_credit_data():
    # Obtém o valor de "count" da query string, ou usa 1 como padrão
    count = int(request.args.get('count', 1))
    
    # Gera a quantidade de dados solicitada
    data = [generate_credit_data() for _ in range(count)]
    
    return jsonify(data), 200, {'Content-Type': 'application/json; charset=utf-8'}

# Executa a API
if __name__ == '__main__':
    app.run(debug=True)
