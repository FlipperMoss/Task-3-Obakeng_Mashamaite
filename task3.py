message = input("Paste email or message here:\n")

message_lower = message.lower()

phishing_keywords = [
    "urgent", "verify", "click here", "password", "bank",
    "free", "account locked", "payment failed",
    "confirm", "winner", "claim now"
]

suspicious_domain = [
    ".xyz", ".tk", "bit.ly", "tinyurl",
    "login-update", "secure-login"
]

score = 0
red_flags = []

for word in phishing_keywords:
    if word in message_lower:
        score += 1
        red_flags.append(word)

for link in suspicious_domain:
    if link in message_lower:
        score += 2
        red_flags.append(link)

if message.isupper():
    score += 1
    red_flags.append("ALL CAPS urgency")

if score >= 5:
    print("Malicious Message")
    print("Reason: Multiple phishing indicators detected")

elif score >= 2:
    print("Suspicious Message")
    print("Reason: Some suspicious characteristics found")

else:
    print("Safe Message")
    print("Reason: No major phishing indicators detected")

print("\nRed Flags Found:")

for flag in red_flags:
    print("-", flag)