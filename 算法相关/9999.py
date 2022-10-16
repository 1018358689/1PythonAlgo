from fake_useragent import UserAgent
import requests
import time
from random import randint

url = 'http://yun.scjsyx.cn/studio/index.php?r=studio/topic/show&sid=300019&id='
ua = UserAgent()
for id in range(228, 256):
    for i in range(55):
        fake_headers = {'User-Agent': ua.random}
        response = requests.get(url=f'{url}{id}', headers=fake_headers)
        print(f'{id}:第{i + 1}次成功！')
        time.sleep(randint(51, 111) / 100)
