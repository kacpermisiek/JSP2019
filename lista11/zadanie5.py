import re
text = "PythonExpressTest"

text2 = (re.sub(r"(\w)([A-Z])", r"\1 \2", text))
print(text2)
