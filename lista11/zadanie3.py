import re
tekst = 'https://github.com/  https://www.wp.pl/'
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+] |[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]|[.]|[/]))+',tekst)
print("Urls: ", urls)
