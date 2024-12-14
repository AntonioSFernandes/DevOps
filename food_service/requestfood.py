from flask import Flask, jsonify, request
from rbanco import pedidos

app = Flask('Pedido')

@app.route('/link-order', methods=['POST'])
def link_order():
    users_data = request.json

    if not isinstance(users_data, list):
        return jsonify({"error": "Formato de dados inválido. Era esperado um objeto JSON."}), 400

    updated_users = []
    for user in users_data:
        
        if 'id' not in user:
            return jsonify({"error": "Usuário possui um *id* inválido"}), 400
        
        matching_order = next((order for order in pedidos if order['id'] == user['id']), None)

        if matching_order:
            user['pedido'] = matching_order['pedido']
        else:
            user['pedido'] = None

        updated_users.append(user)

    return jsonify(updated_users), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
