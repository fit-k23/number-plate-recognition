import requests
from lxml.html import soupparser

encoded_image = {'encoded_image': open("test.png", 'rb')}
captchaurl = 'https://lens.google.com/upload?ep=ccm&s=csp&st=1653142987619'
burp0cap_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
                    "Origin": "null",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "Sec-Gpc": "1", "Sec-Fetch-Site": "none",
                    "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1",
                    "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}
rlens = requests.post(captchaurl, files=encoded_image, headers=burp0cap_headers,allow_redirects=True)

DATA000 = str(rlens.content)
print(DATA000)
root = soupparser.fromstring(DATA000)
result_url = root.xpath('//meta[@http-equiv="refresh"]/@content')
result_url = str(result_url[0])
url2 = result_url.split('URL=')
finalurl = str(url2[1])
print(finalurl)