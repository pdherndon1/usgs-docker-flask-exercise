"""
A simple Flask app to greet visitors.
"""
from hashlib import sha256
from string import hexdigits
from flask import Flask, jsonify
import os
from os import getenv
import dotenv

dotenv.load_dotenv()
app = Flask(__name__)


def create_sha256_hash(name):
    b = bytes(name, 'utf-8')
    hash = sha256(b).hexdigest()
    return hash

"""
Greetings
"""
@app.route('/')
def hell_world():
    return getenv('HELLO')

"""
Return sample JSON data
"""
@app.route('/data')
def data():
    data_json = {"samples":[{"name":"one","id":"7692c3ad3540bb803c020b3aee66cd8887123234ea0c6e7143c0add73ff431ed"},{"name":"two","id":"3fc4ccfe745870e2c0d99f71f30ff0656c8dedd41cc1d7d3d376b0dbe685e2f3"},{"name":"three","id":"8b5b9db0c13db24256c829aa364aa90c6d2eba318b9232a4ab9313b954d3555f"}]}
    four = f"./files/{create_sha256_hash('four')}.txt"
    file_four = open(four, 'w+')
    data_json['samples'].append({'name': 'four', 'id': four})
    return jsonify(data_json)

"""
Runtime
"""
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)