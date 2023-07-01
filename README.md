# ChatGPT-ShellMaster (ChatGPT 4 Plugin)
ChatGPT ShellMaster is a cross-platform (unix/linux) plugin that enables command-line interactions via chat using OpenAI's ChatGPT 4. This powerful tool allows you to run scripts, manage files, and monitor processes directly from your chat interface. It's an excellent tool for developers, making tasks like debugging and file analysis more interactive and intuitive. 

"Please note that access to a developer account and ChatGPT Plus are required to use this plugin. Remember to use this responsibly, being mindful of the security implications".

See [ChatGPT Shellmaster in GPT4](img/shellmaster.png)

## Features
- Execute any Linux/Unix command directly from the ChatGPT interface, effectively transforming your chat into a powerful command-line interface.
- Commands are executed asynchronously, allowing for efficient handling of multiple commands simultaneously, which can greatly aid in debugging and monitoring tasks.
- Fetch files with commands like wget, analyze them, and store the results - all interactively from your chat.
- The working directory for command execution can be configured, providing flexibility while maintaining security precautions.
- Designed to work with temporary directories, enhancing security and reducing the risk of unintentional file manipulation.

### Overview
Logo | Name | System
-- | -- | --
![Logo Cross-Platform Command Execution Plugin](logo.png) |  ChatGPT-ShellMaster Cross-Platform Command Execution Plugin | Unix/linux
![Logo Cross-Platform Command Execution Plugin](logo-cmd.png) | soon! | Windows

## Installation
- Clone this repository to your local machine.
- Install the required Python modules.

```bash
pip install quart
pip install quart-cors
````
Configure the working directory for command execution by editing the settings.json file. The default is /tmp, which is recommended for its safety and security. However, you can modify it as per your needs, ensuring the new directory has a minimum chmod of 700.

## Usage
To get started, run the plugin using the following command:

```python
python3 main.py
```
Next, navigate to your ChatGPT Plus Account. Under Settings, enable the Developer Tools ([see image for reference](img/settings.png)). Switch to the GPT-4 tab and then proceed to the Plugin Store. At the bottom of the Plugin Store page, you'll find a link titled "Develop your own plugin" ([see image](img/pluginshop.png)). Click on this link and enter your information as required.

In my example, I used localhost:5004. You can use another port such as 2323 or 8080, but please ensure that your firewall or security software isn't blocking the connection ([see image](img/load.png)).

To use this plugin, you'll need to send a POST request to the /command endpoint of the server. The request should contain a JSON body with a command field, representing the command you wish to execute.

Example:
```json
{
  "command": "echo 'Hello, World!'"
}
```
Alternatively, you can simplify your workflow by directly instructing ChatGPT, saying: "You have access to my CLI, please execute ...". The rest will be taken care of for you!

The server will execute the command and return the output. If the command fails, the server will return an error message.

## Security
Please be aware that this plugin executes commands as-is, without any sanitization or security checks. Make sure to only use it in a secure and controlled environment, and do not expose the server to the public internet. This ChatGPT Plugin is designed for developers, and should not be deployed on production servers! Use it only on localhost!

## Contributing
Contributions are welcome! Please feel free to submit a pull request.

## Thank you for your support!
If you appreciate my work, please consider supporting me:

- Become a Sponsor: [Link to my sponsorship page](https://github.com/sponsors/volkansah)
- :star: my projects: Starring projects on GitHub helps increase their visibility and can help others find my work. 
- Follow me: Stay updated with my latest projects and releases.

## License
This project is licensed under the "Help the World Grow ❤️ " License . See the [LICENSE](LICENSE) file for details.

## Copyright
[Volkan Kücükbudak](https://gihub.com/volkansah)
[Link to ChatGPT Shellmaster](https://github.com/VolkanSah/ChatGPT-ShellMaster/)

