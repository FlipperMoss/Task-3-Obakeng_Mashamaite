# Task-3-Obakeng_Mashamaite
# Phishing Awareness Analysis Tool

## Project Overview
This project was built as part of my **Week 3 Cybersecurity Internship at DecodeLabs**.

The goal of this project was to create a phishing detection tool that analyzes emails or messages and identifies possible phishing attempts through logical threat analysis.

The tool evaluates messages for suspicious patterns, keywords, and domains that are commonly associated with phishing attacks.

---

## Features

- Detect suspicious phishing keywords
- Detect suspicious domains and URLs
- Identify red flags within messages
- Risk scoring system
- Classify messages into:
  - Safe
  - Suspicious
  - Malicious
- Explain why a message is considered unsafe

---

## How It Works

The program follows a simple analysis process:

1. User enters an email or message
2. The message is converted to lowercase
3. Keywords are checked against known phishing indicators
4. Links/domains are analyzed
5. A score is generated based on findings
6. The message is classified by risk level

---

## Technologies Used

- Python 3

---

## How to Run

### Clone the repository

```bash
git clone https://github.com/your-username/phishing-awareness-tool.git
```

### Navigate into the project folder

```bash
cd phishing-awareness-tool
```

### Run the program

```bash
python main.py
```

---

## Example

### Input

```text
URGENT: Your account has been locked.

Click here:
www.bank-login-update.xyz

Verify your password immediately.
```

### Output

```text
🚨 Malicious Message

Reason: Multiple phishing indicators detected

Red Flags Found:
- urgent
- verify
- password
- account locked
- .xyz
- login-update
```

---

## What I Learned

Through this project I learned:

- Threat analysis fundamentals
- Social engineering awareness
- Pattern recognition in phishing attacks
- Risk scoring systems
- String handling and logic building in Python
- Human-focused cybersecurity principles

---

## Future Improvements

- URL extraction using Regex
- Email header analysis
- Sender reputation checks
- GUI version using Tkinter
- Machine learning classification
- Risk percentage calculations

---

## Internship Project

This project was completed as part of the **DecodeLabs Cybersecurity Internship Program**

---

## 🔗 Connect With Me

LinkedIn: [Your LinkedIn]

GitHub: [Your GitHub]

⭐ Feel free to fork, improve, or star this repository!
