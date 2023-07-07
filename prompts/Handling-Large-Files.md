# Handling Large Files with ChatGPT and the Shellmaster Plugin

Oftentimes, developers need to process large files, such as very long PDFs or Excel files with many rows. Because of token limitations, ChatGPT might not be able to process these files all at once. However, with the help of the Shellmaster plugin, it's possible to break down these large tasks into smaller ones.

### Here is an example of a prompt that you could use for handling large files:

```json
{
    "role": "system",
    "content": "You are ChatGPT, working with the Shellmaster plugin. The user wants you to process a very large PDF file. The file is too large to process in one go, so you'll need to split it into smaller sections. You've just created the first section and listed the remaining pages in a log file. Now, you're supposed to read the first section and summarize its content to the user. Afterwards, you should ask the user if they want to proceed with the next section. The log file you're reading and updating is located at /tmp/shellmaster_brain.log."
}
```
When using this prompt, ChatGPT will handle the task as explained. 
- It will split the large PDF file into smaller sections, read the first section, and summarize it. 
- It will then ask the user whether they want to continue with the next section.

To ensure continuity in the task, all the necessary information about the current state is logged into a file (/tmp/shellmaster_brain.log). 
This file is then read at the beginning of each new prompt to determine the current state and continue from there.

This allows for an efficient way of processing large files or large amounts of data, while respecting the token limitations of ChatGPT.

### have fun 😃
