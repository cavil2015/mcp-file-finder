from flask import Flask, request, jsonify
import os
import time

app = Flask(__name__)

@app.route('/find', methods=['GET'])
def find_files():
    query = request.args.get('query', '')
    search_dir = request.args.get('dir', '.')

    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    results = []
    
    for root, _, files in os.walk(search_dir):
        for file in files:
            if query in file or query in root:
                file_path = os.path.join(root, file)
                file_info = {
                    "name": file,
                    "path": file_path,
                    "size": os.path.getsize(file_path),
                    "created_at": time.ctime(os.path.getctime(file_path))
                }
                results.append(file_info)

    return jsonify(results)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
