import quart_cors
from quart import Quart, request, jsonify, send_file
import asyncio
import os
import sys

app = quart_cors.cors(Quart(__name__), allow_origin="*")

# Betriebssystem erkennen und Arbeitsverzeichnis festlegen
if sys.platform.startswith('win'):
    cwd = "C:\\Users\\DeinBenutzername\\Documents"  # Beispielpfad für Windows
else:
    cwd = "/home/username"  # Beispielpfad für Unix/Linux

@app.route('/read_file', methods=['POST'])
async def read_file():
    data = await request.get_json()
    file_path = data.get("file_path")
    
    if not file_path or not os.path.isfile(file_path):
        return jsonify({"error": "Invalid file path"}), 400
    
    try:
        return await send_file(file_path)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/list_directory', methods=['POST'])
async def list_directory():
    data = await request.get_json()
    directory_path = data.get("directory_path", cwd)
    
    if not os.path.isdir(directory_path):
        return jsonify({"error": "Invalid directory path"}), 400
    
    try:
        files = os.listdir(directory_path)
        return jsonify({"files": files}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/command', methods=['POST'])
async def command():
    data = await request.get_json()
    command = data.get("command")
    
    if not command:
        return jsonify({"error": "No command provided"}), 400
    
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=cwd
    )
    
    stdout, stderr = await process.communicate()
    
    if process.returncode != 0:
        return jsonify({"error": stderr.decode()}), 500
    
    return jsonify({"result": stdout.decode()}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
