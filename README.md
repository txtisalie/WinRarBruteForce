# WinRarBruteForce

WinRarBruteForce is a Python-based utility designed to perform dictionary attacks on password-protected RAR archives. It utilizes the `rarfile` library to automate the process of testing passwords from a provided wordlist against a target file.

## Disclaimer

**EDUCATIONAL USE ONLY.**

This tool is created for security testing, educational purposes, and personal password recovery.
* Do not use this tool on files or systems you do not own.
* The developer assumes no liability for misuse or damage caused by this program.

## Prerequisites

To run this tool, ensure your system meets the following requirements:

1.  **Python 3.x**
2.  **UnRAR Binary:** The `rarfile` library depends on the system having the UnRAR executable.
    * **Windows:** Download `UnRAR.exe` from rarlab.com and place it in the same folder as this script.
    * **Linux:** Install via terminal: `sudo apt-get install unrar`

## Installation

1.  Clone the repository or download the script.
2.  Install the required Python library:

    ```bash
    pip install rarfile
    ```

## Usage

1.  Navigate to the directory containing the script.
2.  Run the application:

    ```bash
    python main.py
    ```

3.  Follow the prompts:
    * **Enter RAR file name:** (e.g., `secure_file.rar`)
    * **Enter password list file:** (e.g., `wordlist.txt`)

## Wordlists

To successfully recover a password, you need a comprehensive wordlist.

**Recommended: RockYou Wordlist**
If you do not have a custom wordlist, the "RockYou" list is the industry standard for testing common passwords.

You can download it directly using the link or command below:

**Direct Link:**
[https://github.com/RykerWilder/rockyou.txt](https://github.com/RykerWilder/rockyou.txt)

**Download via Terminal (curl):**
```bash
curl -L -o rockyou.txt [https://github.com/RykerWilder/rockyou.txt/raw/master/rockyou.txt](https://github.com/RykerWilder/rockyou.txt/raw/master/rockyou.txt)
