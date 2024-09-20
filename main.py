from quart import Quart, request, jsonify, send_file
import asyncio
import os
import sys

app = Quart(__name__)

# Betriebssystem erkennen und Arbeitsverzeichnis festlegen
if sys.platform.startswith('win'):
    # Windows
    cwd = "C:\\Users\\DeinBenutzername\\Documents"  # Beispielpfad für Windows
    shell = True  # Shell-Befehl für Windows
else:
    # Linux/Unix
    cwd = "/home/username"  # Beispielpfad für Unix/Linux
    shell = "/bin/bash"  # Shell-Befehl für Unix/Linux

@app.route('/read_file', methods=['POST'])
async def read_file():
    """
    Liest den Inhalt einer Datei und gibt ihn zurück.
    """
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
    """
    Gibt die Liste der Dateien und Verzeichnisse im angegebenen Pfad zurück.
    """
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
    """
    Führt einen Shell-Befehl aus und gibt die Ausgabe zurück.
    """
    data = await request.get_json()
    command = data.get("command")
    
    if not command:
        return jsonify({"error": "No command provided"}), 400
    
    # Plattformabhängige Anpassung des Befehls
    if sys.platform.startswith('win'):
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=cwd
        )
    else:
        process = await asyncio.create_subprocess_exec(
            shell, '-c', command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=cwd
        )
    
    stdout, stderr = await process.communicate()
    
    if process.returncode != 0:
        return jsonify({"error": stderr.decode()}), 500
    
    return jsonify({"result": stdout.decode()}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)
