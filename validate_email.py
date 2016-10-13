"""
Title: Validating Email Addresses With a Filter
Description: You are given an integer N followed by N email addresses. Your task 
is to print a list containing only valid email addresses in lexicographical order.

Valid email addresses must follow these rules:

- It must have the username@websitename.extension format type.
- The username can only contain letters, digits, dashes and underscores.
- The website name can only have letters and digits.
- The maximum length of the extension is 3.
"""

import re

def validate_email(N, emails):

    l = []
    for email in emails:

        email_splitted = email.split('@')
        if(len(email_splitted) == 2):
            username = email_splitted[0]
            website = email_splitted[1]
        else:
            continue

        website_splitted = website.split('.')
        if(len(website_splitted) == 2):
            websitename = website_splitted[0]
            extension = website_splitted[1]
        else:
            continue

        if(
            re.match("^[a-zA-Z0-9-_]+$", username, re.I) and
            re.match("^[a-zA-Z0-9]+$", websitename, re.I) and
            len(extension) <= 3
        ):
            l.append(email)

    return sorted(l)

N = int(raw_input().strip())
emails = []
for i in range(N):
    emails.append(str(raw_input().strip()))

print validate_email(N, emails)
