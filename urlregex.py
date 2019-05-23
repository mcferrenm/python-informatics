# Search for link values within URL input
import urllib
import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.urlopen(url).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
	print(link.decode())
