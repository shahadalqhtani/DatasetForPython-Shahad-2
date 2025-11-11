bash
pip install flask pyyaml
from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    payload = request.get_json()  # Get JSON data from the POST request
    if 'type' in payload and payload['type'] == 'Create':
        return jsonify({'error': 'Creation not allowed'}), 403
    else:
        try:
            yaml_payload = yaml.safe_load(request.data)
            # Here you can add more processing for the YAML payload if needed
            return jsonify(yaml_payload), 200
        except Exception as e:
            return jsonify({'error': 'Invalid YAML format', 'details': str(e)}), 400

if __name__ == '__main__':
    app.run(port=5000)
bash
python app.py
bash
curl -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d '{"type": "Create", "name": "John
Doe"}'