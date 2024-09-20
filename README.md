
# ⭐ ChatGPT-ShellMaster (Custom GPT Integration) ⭐
#### Updated 20.09.2024 dev-status!

![ChatGPT Shellmaster](img/chatgpt-shellmaster1.png)

ChatGPT ShellMaster is a cross-platform (Windows/Unix/Linux) integration for OpenAI's ChatGPT. It transforms your chat into a powerful command-line interface (CLI) for executing scripts, managing files, and monitoring processes.

⚠️ **Note:** This version is similar to ChatGPT ShellMaster Version 1, but OpenAI no longer supports plugins. The new version of ShellMaster is now under development as a Custom GPT integration. To use this integration, you need to start a Quart server locally and then access the Custom GPT Store link provided below to establish the connection.

## How to Use

1. **Start the Quart Server Locally:**
   - Run the Quart server on your machine using the following command:
   ```bash
   python3 main.py
   ```
   - Ensure that your firewall or security software allows the connection to the specified port (default: 5000).

2. **Access the Custom GPT Link:**
   - Click on the link below to access the Custom GPT integration. Provide your local server's IP address and port (e.g., `localhost:5000`) to establish the connection.
   - [GPT ShellMaster Link](#) (soon!)

3. **Establish the Connection:**
   - Once connected, you can use ChatGPT to interact with your local environment. The GPT will send HTTP requests to your local server to execute commands, read files, and manage directories.

## Features

- Execute Windows/Unix/Linux commands directly from the ChatGPT interface.
- Handle multiple commands simultaneously with asynchronous execution.
- Fetch, analyze, and store files interactively from your chat.
- Configure the working directory for command execution to ensure flexibility and security.
- Works with temporary directories to reduce the risk of unintentional file manipulation.
- Learn system commands with interactive guides.

## Installation

- Clone this repository to your local machine.
- Install the required Python modules:
    ```bash
    pip install quart
    pip install quart-cors
    ```

## Configuration

- Configure the working directory in the code for Windows or Linux/Unix. This Quart server runs on multiple platforms.

## Security

Please be aware that this integration executes commands as-is, without any sanitization or security checks. Use it only in a secure and controlled environment, and do not expose the server to the public internet. This Custom GPT integration is designed for local use only. 

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## ❤️ Thank you for your support!

If you appreciate my work, please consider supporting me:

- Become a Sponsor: [Link to my sponsorship page](https://github.com/sponsors/volkansah)
- :star: my projects: Starring projects on GitHub helps increase their visibility and can help others find my work.
- Follow me: Stay updated with my latest projects and releases.

### 👣 Other GPT projects 

- [GPT-Security-Best-Practices](https://github.com/VolkanSah/GPT-Security-Best-Practices)
- [OpenAi cost calculator](https://github.com/VolkanSah/OpenAI-Cost-Calculator)
- [GPT over CLI](https://github.com/VolkanSah/GPT-over-CLI)
- [Secure Implementation of Artificial Intelligence (AI)](https://github.com/VolkanSah/Implementing-AI-Systems-Whitepaper)
- [Comments Reply with GPT (davinci3)](https://github.com/VolkanSah/GPT-Comments-Reply-WordPress-Plugin)
- [Basic GPT Webinterface](https://github.com/VolkanSah/GPT-API-Integration-in-HTML-CSS-with-JS-PHP)
- [Exploring the Code Interpreter in OpenAI](https://github.com/VolkanSah/The-Code-Interpreter-in-OpenAI-ChatGPT)

### License

This project is licensed under the "Help the World Grow [💔](https://jugendamt-deutschland.de)" License. See the [LICENSE](LICENSE) file for details.

- [Source of this repository](https://github.com/VolkanSah/ChatGPT-ShellMaster)
