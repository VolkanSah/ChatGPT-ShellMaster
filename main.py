import asyncio
import sys
import json
import logging
import requests
import quart
import quart_cors
from quart import request

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load settings
with open("settings.json") as f:
    settings = json.load(f)
cwd = settings.get("working_directory", ".")

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")


@app.get("/logo.png")
async def plugin_logo():
    """
    Serve the plugin logo.

    This function returns the logo.png file to the client.
    """
    filename = "logo.png"
    return await quart.send_file(filename, mimetype="image/png")

@app.post("/command")
async def command():
    """
    Execute a shell command and return the output.

    This function receives a JSON request with a "command" field, executes the command,
    and returns the output. If the command fails, the function returns the error message.
    """
    data = await request.get_json()
    command = data.get("command")
    if not command:
        return quart.Response(response="No command provided", status=400)
    logging.info(f"Received command: {command}")

    # Use asyncio to execute the command
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=cwd)

    stdout, stderr = await process.communicate()

    # Check for errors
    if process.returncode != 0:
        return quart.Response(response=stderr.decode("utf-8"), status=500)
    else:
        return quart.Response(response=stdout.decode("utf-8"), status=200)


@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    """
    Serve the plugin manifest.

    This function reads the ai-plugin.json file and returns it to the client.
    """
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")


@app.get("/openapi.yaml")
async def openapi_spec():
    """
    Serve the OpenAPI specification.

    This function reads the openapi.yaml file and returns it to the client.
    """
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

if __name__ == "__main__":
    # Run the Quart application
    app.run(debug=True, host="0.0.0.0", port=5004)
