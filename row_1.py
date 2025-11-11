bash
pip install flask
from flask import Flask, request, jsonify
import urllib.parse

app = Flask(__name__)

def redirect_url(url):
    parsed_url = urllib.parse.urlparse(url)
    domain_name = parsed_url.netloc

    if domain_name == 'example.com':
        return jsonify({'redirect': url}), 200
    else:
        return "Not Found", 404

@app.route('/redirect', methods=['POST'])
def handle_redirect():
    data = request.get_json()
    if 'url' not in data:
        return jsonify({'error': 'Missing URL parameter'}), 400

    url = data['url']
    response = redirect_url(url)
    return response

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)
bash
curl -X POST http://localhost:5000/redirect -H "Content-Type: application/json" -d '{"url":
"https://example.com/"}'