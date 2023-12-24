import math
import random
from base64 import b64encode

import requests

def generateRandomString(n):
    ls = "abcdefghijklmnopqrstuvwxyz0123456789"
    s = ""
    for _ in range(n):
        s += ls[math.floor(random.random() * len(ls))]
    return s

def requestImage(imageFile):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4725.0 Safari/537.36"
    }
    body = {
        "image_url": "https://" + generateRandomString(12) + ".com/images/" + generateRandomString(12),
        "sbisrc": "Chromium 98.0.4725.0 Windows"
    }
    files = {
        'encoded_image': imageFile
    }
    result = requests.post(f'https://lens.google.com/upload?ep=ccm&s=&st=' + generateRandomString(12), headers=headers, data=body, files=files)
    if result.status_code == 200:
        print(result.text)
        s = result.text
        h1 = "url="
        l = s.find(h1) + len(h1)
        f1 = "\">"
        uri = s[l:s.find(f1, l)]
        url = "https://lens.google.com" + uri
        return url
    return None

def getPlate(gLenUrl):
    r = requests.get(gLenUrl)

    start0 = "AF_initDataCallback"
    start1 = "UNIFIED_GRID"
    start2 = "text:0"
    start3 = "\",[[[\""

    end = "\"]],\""
    with open('data.html', 'w') as f:
        f.write(r.text)
    sp = r.text.find(start0)
    if sp == -1:
        return ""
    sp = r.text.find(start1, sp)
    sp = r.text.find(start2, sp)
    sp = r.text.find(start3, sp)
    ep = r.text.find(end, sp)

    return r.text[sp + len(start3):ep].split("\",\"")
image = "https://metalbyexample.com/wp-content/uploads/figure-65.png"
image_filename = "test.png"

def get_base64_image(url):
    r = requests.get(url, stream=True)
    img_uri = ("data:" +
           r.headers['Content-Type'] + ";" +
           "base64," + b64encode(r.content).decode())

    return img_uri

# file = open(image_filename, mode='rb')
file = get_base64_image(image)
# print(file.read())

print(requests.put("https://lens.google.com/uploadbyurl?hl=en&lr=en&url=" + image, allow_redirects=True).url)

r = requestImage(file)

print(r)

if r is None:
    print("No url")
    exit()
print("\"" + getPlate(r) + "\"")