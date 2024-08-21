# 📧 EmailVerifier

**EmailVerifier** is a Python-based tool designed to validate and verify email addresses by checking their syntax, domain, and SMTP status. It helps you ensure that the emails in your lists are valid and reachable, reducing the likelihood of bounced emails and improving your email campaign efficiency.

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
    source venv/bin/activate  # On Windows use venv\\Scripts\\activate


### 3. **Install the required dependencies**:
    
    pip install -r requirements.txt
    

## 🛠️ Usage

You can use EmailVerifier to validate single or multiple email addresses. Below is a summary of the available command-line options:

    python main.py [-h] [-o OUTPUT] [-s SUSPICIOUS] [-d DELAY] [-t THREADS] [-e EMAIL] [input]


## 💡 Examples

### 1. **Verify a single email address**:
    python main.py -e example@example.com
    

### 2. **Verify emails from a file and save valid emails to a file**:
    python main.py input.txt -o valid_emails.txt


### 3. **Verify emails from a file with a delay of 2 seconds between requests**:
    python main.py input.txt -d 2


### 4. **Verify emails using 8 threads for faster processing**:
    python main.py input.txt -t 8


### 5. **Save suspicious email addresses to a separate file**:
    python main.py input.txt -s suspicious_emails.txt



## 📂 Project Structure

- **main.py**: The entry point of the application.
- **email_verifier/smtp_verifier.py**: Handles the SMTP verification logic.
- **email_verifier/file_handler.py**: Manages file operations for reading emails from files.
- **email_verifier/config.py**: Contains the configuration settings for the application.
- **email_verifier/checker.py**: Core logic for validating email syntax and domain.


## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push the branch to your fork.
5. Open a Pull Request.