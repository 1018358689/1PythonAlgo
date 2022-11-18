from selenium import webdriver

import time
from random import randint
import datetime
# from fake_useragent import UserAgent

# ua = UserAgent()
# for _ in range(10):
#     print(ua.random)
opt = webdriver.ChromeOptions()
opt.add_argument('--ignore-certificate-errors')
# opt.add_argument('--ignore-ssl-errors')
# opt.add_argument(f'--user-agent={ua.random}')


# 判断当前时间是否在（starTime~endTime）时间范围内
def isDuringThatTime(startTime, endTime):
    start_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + startTime, '%Y-%m-%d%H:%M')
    end_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + endTime, '%Y-%m-%d%H:%M')
    now_time = datetime.datetime.now()
    return start_time <= now_time <= end_time


for id in range(311, 312):
    #1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
    browser = webdriver.Chrome(executable_path="E:\chromedriver", options=opt)
    #2.通过浏览器向服务器发送URL请求
    browser.get(f'http://yun.scjsyx.cn/studio/index.php?r=studio/topic/show&sid=300019&id={id}')
    browser.implicitly_wait(3)
    # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    cnt = 0
    #3.刷新浏览器
    while not isDuringThatTime("23:58", "23:59") and cnt < 23:
        cnt += 1
        browser.refresh()
        # for i in range(10):
        #     browser.execute_script(f'document.documentElement.scrollTop={(i+1)*1000}')

        t = randint(123, 999) / 1000
        time.sleep(t)
        print(f'{cnt} - {t} - {datetime.datetime.now()}')
    print(cnt)
    browser.close()
    browser.quit()
