#!/usr/bin/python

# @File : SeleniumUtils.py
# @Author: 邵泽铭
# @Date : 18-10-16
# @Desc :
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
import time
from lxml import etree




class SeleniumUtils:
    @staticmethod
    def getEndHtml(url):
        driver = webdriver.Firefox()
        driver.get(url)
        try:
            time.sleep(10)
            html=driver.page_source
            return etree.HTML(html)
        except Exception as e:
            print(e)

        finally:
            driver.close()
            driver.quit()


