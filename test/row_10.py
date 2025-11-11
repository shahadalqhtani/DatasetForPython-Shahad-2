from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route('/handle-payload', methods=['POST'])
def handle_payload():
    payload = request.json.get('payload')

    if not payload:
        return jsonify({"error": "Payload is missing"}), 400

    try:
        data = yaml.safe_load(payload)
    except yaml.YAMLError as e:
        return jsonify({"error": f"Invalid YAML format: {e}"}), 400

    if not isinstance(data, dict):
        return jsonify({"error": "Payload must be a dictionary"}), 400

    type_value = data.get('type')
    if not type_value:
        return jsonify({"error": "Type is missing in payload"}), 400

    if type_value == 'Create':
        return jsonify({"response": f"Received Create request with details: {data}"}), 200
    elif type_value == 'Update':
        name = data.get('name')
        if not name or name != 'UnsafeDeserialization':
            return jsonify({"error": "Invalid name for update request"}), 400
        else:
            return jsonify({"response": f"Received Update request with details: {data}"}), 200
    else:
        return jsonify({"error": "Unsupported type"}), 400

if __name__ == '__main__':
    app.run(port=5000)