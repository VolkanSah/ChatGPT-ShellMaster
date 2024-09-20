import requests

class LocalAssistant:
    def __init__(self):
        self.server_url = "http://localhost:5000"

    def execute_command(self, command):
        """Führt einen Shell-Befehl auf dem lokalen System aus."""
        url = f"{self.server_url}/command"
        data = {"command": command}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()["result"]
        else:
            return f"Fehler: {response.json()['error']}"

    def read_file(self, file_path):
        """Liest den Inhalt einer Datei."""
        url = f"{self.server_url}/read_file"
        data = {"file_path": file_path}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.text
        else:
            return f"Fehler: {response.json()['error']}"

    def list_directory(self, directory_path):
        """Listet die Dateien und Verzeichnisse in einem Verzeichnis auf."""
        url = f"{self.server_url}/list_directory"
        data = {"directory_path": directory_path}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()["files"]
        else:
            return f"Fehler: {response.json()['error']}"
