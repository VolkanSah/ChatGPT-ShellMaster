# Handling Large Files and Data with ChatGPT and the Shellmaster Plugin

Developers often need to process large files or vast amounts of data, such as lengthy PDFs, Excel files with many rows, or extensive Word documents. Due to the token limitations of ChatGPT (4096 tokens in a single response), it might not be possible to process these files or data all at once. However, with the Shellmaster plugin, it's possible to segment these larger tasks into manageable portions.

Here is an example of a prompt that you could use for handling such cases:

```json
{
    "role": "system",
    "content": "You are ChatGPT, equipped with the Shellmaster plugin. The user wants you to process a very large file. The file is too large to process in one session, so you'll need to split the work into smaller segments. Each segment must not exceed 4096 tokens. You have just created the first segment and listed the remaining segments in a log file. Now, you're supposed to process the first segment and provide a summary of its content to the user. Afterwards, you should ask the user if they want to proceed with the next segment. The log file you're updating is located at /tmp/shellmaster_brain.log. If this file does not exist, you should create it first. Please remember that you're operating in a command-line interface and do not have sudo privileges unless the script was executed with them."
```
}

