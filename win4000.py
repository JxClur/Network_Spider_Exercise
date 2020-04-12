import requests
import re
import time
import os
from lxml import etree


def getOnePage(n):
    """Web Requests"""
    html = f'http://www.win4000.com/wallpaper_detail_167506_{n}.html'
#    html = f'http://www.win4000.com/wallpaper_detail_167{n}_*.html'
    hd = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
    response = requests.get(html,headers=hd)
    return response.text


def parse(html):
    """Content Traverse"""
#html_xpath = etree.HTML()
#html_xpath.xpath()
    url = re.findall('<img class=".*?" src="(.*?)" alt=".*?" title=".*?"/>',html)
    print(url)
    return url

    # response = requests.get(url, headers=hd)
    # with open(dir_name + '/'+ pic_name, 'wb') as f:
    #     f.write(response.content)

def save2pic(url):
    """Save Pictures"""
#    dir_name = re.findall('<h1>(.*?)</h1>', html)[-1]
#     if not os.path.exists(dir_name):
#         os.mkdir(dir_name)
    print(url)
    pic_name = url.split('/')[-1]
    hd = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
    response = requests.get(url,headers=hd)
    with open(pic_name, 'wb') as f:
        f.write(response.content)

def run():
    for n in range(0,11):
        html = getOnePage(n)
        items = parse(html)
        for item in items:
            save2pic(item)

if __name__ == "__main__":
    run()
