# Email Header Analyzer

## 📌 Overview

The **Email Header Analyzer** is a CLI tool that extracts and analyzes email headers from `.eml` files to detect phishing attempts. It checks for SPF, DKIM, and DMARC authentication failures to identify potential email spoofing.

## 🚀 Features

- Extracts key email headers such as **From, To, Subject, Date, and Message-ID**.
- Analyzes **SPF, DKIM, and DMARC** authentication results.
- Detects common phishing indicators and warns about suspicious emails.
- Simple **command-line interface (CLI)** for easy usage.

## 🛠 Installation

Ensure you have **Python 3.x** installed. Then, install dependencies:

```bash
pip install argparse
```

## 📥 Usage

Run the tool by providing an `.eml` email file:

```bash
python email_analyzer.py sample.eml
```

### 📝 Example Output

```
Extracted Headers:
From: sender@example.com
To: recipient@example.com
Subject: Urgent Account Verification
Date: Fri, 22 Mar 2025 10:30:00 GMT
SPF: fail
DKIM: pass
DMARC: fail

Security Analysis:
⚠ SPF validation failed: Possible spoofing attempt.
⚠ DMARC policy failure: Email may not be from a trusted source.
```

## 🔐 Security Notes

- This tool is for **educational and research purposes** only.
- Always verify email sources before clicking on links or downloading attachments.

## 🏆 Contributing

Feel free to open issues or submit pull requests to enhance this tool!

## 📜 License

This project is licensed under the **MIT License**.
