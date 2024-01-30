import re

text = """
"hola@email.com, hola2@email.com, email3@cee.carx.com.br
"""

pattern = r"[\w%+-.]+@[\w]+\.[a-zA-Z.]+"
emails_match = re.findall(pattern, text)
emails = list(set(emails_match))

from pprint import pformat
print(pformat(emails))
