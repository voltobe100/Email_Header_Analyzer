import email
import re
import argparse
from email import policy
from email.parser import BytesParser

def extract_email_headers(file_path):
    with open(file_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)
    
    headers = {
        "From": msg.get("From"),
        "To": msg.get("To"),
        "Subject": msg.get("Subject"),
        "Date": msg.get("Date"),
        "Return-Path": msg.get("Return-Path"),
        "Received": msg.get_all("Received"),
        "Message-ID": msg.get("Message-ID"),
        "SPF": msg.get("Authentication-Results"),
        "DKIM": msg.get("DKIM-Signature"),
        "DMARC": msg.get("Authentication-Results"),
    }
    return headers

def detect_spoofing(headers):
    issues = []
    
    if headers["SPF"] and "fail" in headers["SPF"].lower():
        issues.append("⚠ SPF validation failed: Possible spoofing attempt.")
    
    if headers["DKIM"] and "fail" in headers["DKIM"].lower():
        issues.append("⚠ DKIM signature failed: Message integrity may be compromised.")
    
    if headers["DMARC"] and "fail" in headers["DMARC"].lower():
        issues.append("⚠ DMARC policy failure: Email may not be from a trusted source.")
    
    return issues if issues else ["✅ No immediate spoofing threats detected."]

def main():
    parser = argparse.ArgumentParser(description="Analyze email headers for phishing detection.")
    parser.add_argument("file", help="Path to the .eml email file")
    args = parser.parse_args()
    
    headers = extract_email_headers(args.file)
    print("\nExtracted Headers:")
    for key, value in headers.items():
        print(f"{key}: {value}")
    
    print("\nSecurity Analysis:")
    for issue in detect_spoofing(headers):
        print(issue)

if __name__ == "__main__":
    main()
