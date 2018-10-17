#!/usr/bin/python

# @File : pictest.py
# @Author: 邵泽铭
# @Date : 10/11/18
# @Desc :




import pytesseract
from PIL import Image
import requests
from lxml import etree
import time
import uuid
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import subprocess
#

# driver.implicitly_wait(10)
driver = webdriver.Firefox()
for i in range(100):
    driver.get("http://ip.zdaye.com/FreeIPlist.html")
    # el = driver.find_element_by_id("ipc")
    # print(els[0].get_attribute("href"))


    try:
        WebDriverWait(driver, 30).until(lambda x: x.find_element_by_id("ipc"))
        cos = driver.get_cookies()
        print(cos)

        acw_tc = driver.get_cookie("acw_tc")[0]["value"]
        acw_sc__v2 = driver.get_cookie("acw_sc__v2")[0]["value"]
        acw_sc__v3 = driver.get_cookie("acw_sc__v3")[0]["value"]

        #
        # driver.add_cookie(cos[0])
        # driver.get("http://ip.zdaye.com/FreeIPlist.html")
        # cos3=driver.get_cookies()
        #

        # print(cos3)
        s = requests.Session()
        response = s.get("http://ip.zdaye.com/FreeIPlist.html",
                         cookies={"acw_tc": acw_tc, "acw_sc__v2": acw_sc__v2, "acw_sc__v3": acw_sc__v3})
        print(response.text)

        headers = {
            "Referer": "http://ip.zdaye.com/FreeIPlist.html",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
            'Connection': 'close'
        }
        selector = etree.HTML(response.text)
        res = selector.xpath("// *[ @ id = 'ipc'] / tbody / tr / td / img")
        for re in res:
            path = re.xpath("./@src")[0]
            response2 = s.get("http://ip.zdaye.com" + path, headers=headers)
            name = str(datetime.timestamp(datetime.utcnow())).replace(".", "")
            content = response2.content
            with open("./img1/" + name + '.bmp', 'wb') as f:
                f.write(content)

        time.sleep(2)

    finally:
        driver.close()





# tessdata_dir_config = '--tessdata-dir "/usr/local/share/tessdata"'
#
# # 二值化
# threshold = 140
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
#
# # 由于都是数字
# # 对于识别成字母的 采用该表进行修正
# rep = {'O': '0',
#        'I': '1', 'L': '1',
#        'Z': '2',
#        'S': '8'
#        }
#
#
# def getverify1(name):
#     # 打开图片
#     im = Image.open(name)
#     # 转化到灰度图
#     imgry = im.convert('L')
#     # 保存图像
#     imgry.save('g' + name)
#     # 二值化，采用阈值分割法，threshold为分割点
#     out = imgry.point(table, '1')
#     out.save('b' + name)
#     # 识别
#     text = pytesseract.image_to_string(out,config=tessdata_dir_config)
#     # 识别对吗
#     text = text.strip()
#     text = text.upper()
#     for r in rep:
#         text = text.replace(r, rep[r])
#         # out.save(text+'.jpg')
#     print(text)
#
#
# getverify1("a.bmp")