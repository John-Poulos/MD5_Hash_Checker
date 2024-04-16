from flask import Flask, request, jsonify
import hashlib
import os

app = Flask(__name__)

def calculate_md5(file):
    hash_md5 = hashlib.md5()
    with file as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

@app.route('/md5', methods=['POST'])
def get_md5():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided."}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file."}), 400
    
    try:
        md5_hash = calculate_md5(file)
        return jsonify({"md5": md5_hash})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/authenticate', methods=['POST'])
def authenticate():
    if 'file' not in request.files or 'hash' not in request.form:
        return jsonify({"error": "Both file and hash are required."}), 400
    file = request.files['file']
    user_hash = request.form['hash']
    
    if len(user_hash) != 32:
        return jsonify({"error": "Invalid hash length. MD5 hash should be 32 characters long."}), 400
    
    try:
        md5_hash = calculate_md5(file)
        if md5_hash == user_hash:
            return jsonify({"result": "Authenticated"})
        else:
            return jsonify({"result": "Failed to Match!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return 'Welcome to the MD5 Hash Calculator!'

if __name__ == "__main__":
    app.run(debug=False)