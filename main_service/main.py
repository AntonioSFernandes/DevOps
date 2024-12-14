from flask import Flask, make_response, jsonify, request
from ubanco import users

app = Flask('GenUser')

@app.route('/users', methods=['GET'])
def get_user():
    return make_response(jsonify(users), 200)

@app.route('/users', methods=['POST'])
def create_users():
    new_user = request.json
    
    if not isinstance(new_user, dict):
        return make_response(jsonify({'error': 'Formato de dados inválido. Era esperado um objeto JSON.'}), 400)
    
    users.append(new_user)
    return make_response(jsonify({'message': 'Usuário adicionado com sucesso!', 'user': new_user}), 201)

@app.route('/sync-request', methods=['POST'])
def sync_request():
    try:
        response = request.post('http://food_service:5001/link-order', json=users)
        response.raise_for_status()
    except request.RequestException as e:
        return jsonify({"error": f"Falha ao sincronizar pedido: {str(e)}"}), 500

    return jsonify(response.json()), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

