# ChatGPT-ShellMaster
ChatGPT ShellMaster is a cross-platform plugin that enables command-line interactions via chat using OpenAI's ChatGPT. This powerful tool allows you to run scripts, manage files, and monitor processes directly from your chat interface. It's an excellent tool for developers, making tasks like debugging and file analysis more interactive and intuitive. Please note that access to a developer account and ChatGPT Plus are required to use this plugin. Remember to use this responsibly, being mindful of the security implications.

## Features
- Execute any Linux/Unix command directly from the ChatGPT interface, effectively transforming your chat into a powerful command-line interface.
- Commands are executed asynchronously, allowing for efficient handling of multiple commands simultaneously, which can greatly aid in debugging and monitoring tasks.
- Fetch files with commands like wget, analyze them, and store the results - all interactively from your chat.
- The working directory for command execution can be configured, providing flexibility while maintaining security precautions.
- Designed to work with temporary directories, enhancing security and reducing the risk of unintentional file manipulation.
## Installation
- Clone this repository to your local machine.
- Install the required Python modules.

```bash
pip install quart
pip install quart-cors
````
Configure the working directory for command execution by editing the settings.json file. The default is /tmp, which is recommended for its safety and security. However, you can modify it as per your needs, ensuring the new directory has a minimum chmod of 700.

## Usage
To use this plugin, you need to send a POST request to the /command endpoint of the server. The request should contain a JSON body with a command field, which is the command you want to execute.

### Example:

```json
{
  "command": "echo 'Hello, World!'"
}
```

Or, to streamline your workflow, you can simply say to ChatGPT "You have access to my CLI, please execute ...", and the rest is handled for you!

The server will execute the command and return the output. If the command fails, the server will return an error message.

## Security
Please be aware that this plugin executes commands as-is, without any sanitization or security checks. Make sure to only use it in a secure and controlled environment, and do not expose the server to the public internet. This ChatGPT Plugin is designed for developers, and should not be deployed on production servers! Use it only on localhost!

## Contributing
Contributions are welcome! Please feel free to submit a pull request.

## License
This project is licensed under the "Help the World Grow ❤️ " License . See the [LICENSE](LICENSE) file for details.

## Overview
Logo | Name | System
-- | -- | --
![Logo Cross-Platform Command Execution Plugin](logo.png) |  Cross-Platform Command Execution Plugin | Unix/linux
![Logo Cross-Platform Command Execution Plugin](logo-cmd.png) | soon! | Windows
