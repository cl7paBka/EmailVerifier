# 📧 EmailVerifier

**EmailVerifier** is a Python-based tool designed to validate and verify email addresses by checking their syntax,
domain, and SMTP status. It helps you ensure that the emails in your lists are valid and reachable, reducing the
likelihood of bounced emails and improving your email campaign efficiency.

## ✨ Features

- ✅ **Email Syntax Validation**: Checks if the email format adheres to the standard format.
- 🌐 **Domain Verification**: Verifies if the email domain is valid and active.
- 📬 **SMTP Verification**: Connects to the SMTP server to validate if the email address is deliverable.
- 📂 **Bulk Email Verification**: Supports verifying multiple emails from a file.
- ⚙️ **Configurable Settings**: Allows customization through a configuration file.
- 📝 **Logging and Reporting**: Provides detailed logs and results for your verifications.

## 🚀 Installation

### 1. **Clone the repository**:
    
    git clone https://github.com/cl7paBka/EmailVerifier.git
    cd EmailVerifier
    

### 2. **Create and activate a virtual environment** (optional but recommended):
    
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`


### 3. **Install the required dependencies**:
    
    pip install -r requirements.txt
    
## 🛠️ Usage

[![Email-Verifier-h.png](https://i.postimg.cc/brX4dHtk/Email-Verifier-h.png)](https://postimg.cc/5Y3sRzp2)

You can use EmailVerifier to validate single or multiple email addresses. Below is a summary of the available
command-line options:

    python EV.py [-h] [-o OUTPUT] [-s SUSPICIOUS] [-d DELAY] [-t THREADS] [-e EMAIL] [input]

## 💡 Examples

### 1. **Verify a single email address**:

    python EV.py -e example@example.com
[![Email-Verifier-1email.png](https://i.postimg.cc/MGvLDr01/Email-Verifier-1email.png)](https://postimg.cc/R3xGCdD0)

### 2. **Verify emails from a file, save valid and suspicious addresses to separate files**:

    python EV.py "\path\to\your\input_file.txt" -o "\path\to\your\validated_adresses.txt" -s s"\path\to\your\suspicious_adresses.txt

### 3. **Verify emails from a file with a delay of 2 seconds between requests using 8 threads for faster processing**:

    python EV.py "\path\to\your\input_file.txt" -d 2 -t 8

### 4. **Verify emails from src/files/input.txt, save valid to src/files/validated_addresses.txt and suspicious to src/files/suspicious_addresses.txt**

    python EV.py 

[![Email-Verifier-example.png](https://i.postimg.cc/t420DxKG/Email-Verifier-example.png)](https://postimg.cc/sMQ0gvfT)

### 5. **To stop program press CTRL+C"**

[![Email-Verifier-CTRL-C.png](https://i.postimg.cc/rsJgcSC8/Email-Verifier-CTRL-C.png)](https://postimg.cc/8f7Lmf03)


## 📂 Project Structure

```Bash
EmailVerifier/
│
├── src/                      # Source folder containing core logic
│   ├── files/                # Folder for input and output .txt files
│   │   ├── input.txt         # Input file containing email addresses
│   │   ├── suspicious_addresses.txt # Output file for suspicious email addresses
│   │   └── validated_addresses.txt  # Output file for validated email addresses
│   │
│   ├── checker.py            # Module to check and verify emails
│   ├── config.py             # Configuration settings for the application
│   ├── file_handler.py       # File handling utilities for input/output operations
│   ├── smtp_verifier.py      # Module for SMTP-based email verification
│   └── utils.py              # Utility functions for various helper tasks   
│
├── EV.py                     # Main entry point script to run the EmailVerifier
│
└── README.md                 # Project overview, structure, and usage instructions
```

### 📚 Description of Key Components:

- **src/files/**: This directory contains `.txt` files used as input and output for email addresses:
    - `input.txt`: Contains the list of email addresses to be verified.
    - `suspicious_addresses.txt`: Stores suspicious email addresses (e.g., from B2C providers).
    - `validated_addresses.txt`: Stores successfully validated email addresses.

- **src/checker.py**: Core logic for processing and verifying email addresses.

- **src/config.py**: Stores configuration settings, such as delays between SMTP requests, thread counts, etc.

- **src/file_handler.py**: Provides helper functions to read/write from/to files.

- **src/smtp_verifier.py**: Handles SMTP verification of email addresses, connecting to mail servers to validate them.

- **src/utils.py**: Shows logo and colors words.

- **EV.py**: The main script to run the EmailVerifier tool, parsing command-line arguments and managing the flow of the
  application.

- **README.md**: The readme file contains a detailed project overview, instructions, and usage guidelines.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push the branch to your fork.
5. Open a Pull Request.