import requests
import re
import time
import os

"""Web Requests"""
hd = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
response = requests.get("https://www.vmgirls.com/12234.html",headers=hd)
#print(response.request.headers)
html = response.text


"""Content Traverse"""
dir_name = re.findall('<h1 class="post-title h3">(.*?)</h1>',html)[-1]
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">',html)

print(urls)

"""Save Pictures"""

for url in urls:
    time.sleep(1)
    pic_name = url.split('/')[6]
    response = requests.get(url, headers=hd)
    with open(dir_name + '/'+ pic_name, 'wb') as f:
        f.write(response.content)