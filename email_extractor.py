import re

print("Email Extractor")
print("----------------")

with open("sample.txt", "r") as file:
    text = file.read()

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(email_pattern, text)

print("Email addresses found:")

for email in emails:
    print(email)

with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print()
print("Email addresses saved to emails.txt")