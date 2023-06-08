# Exercise: https://www.hackerrank.com/challenges/validating-named-email-addresses
import email.utils
import re

pattern_name = r"^[a-zA-Z\s]+"
pattern_email = r"<[a-zA-Z][\w.+-]+@[a-zA-Z]+[.]?\.[a-zA-Z]{1,3}>"

for _ in range(int(input())):
    string = input()

    find_name = re.search(pattern_name, string)
    find_email = re.search(pattern_email, string)

    if find_name is not None and find_email is not None:
        name = find_name.group().strip()
        email_address = find_email.group().strip("<").strip(">")

        formatted_address = email.utils.formataddr((name, email_address), charset='utf-8')

        print(formatted_address)
