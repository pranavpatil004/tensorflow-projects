import re
import requests


pattern = re.compile("and the next nothing is (\d+)")
num = 16044
while True:
    res = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(num))
    content = res.text
    print(content)
    match = pattern.search(content)
    if match == None:
        if (re.compile('Yes. Divide by two and keep going').search(content) == None):
            break
        else:
            num = int(num) / 2
    else:
        num = match.group(1)