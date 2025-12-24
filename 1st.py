import re
text = "My email is test123@gmail.com"
pattern = r'\w+@\w+\.\w+'
match = re.search(pattern, text)
if match:
    print("Matched:", match.group())
else:
    print("not matched")
