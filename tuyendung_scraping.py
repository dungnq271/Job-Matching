from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selectolax.parser import HTMLParser

import itertools
from pprint import pprint
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from functools import partial


options = Options()
options.add_experimental_option("detach", True)  # keep the window open

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = \
"""
https://www.google.com/search?channel=fs&client=ubuntu-sn&q=ai+engineer+tuy%E1%BB%83n+d%E1%BB%A5ng&ibp=htl;jobs&sa=X&ved=2ahUKEwizqofEs_qEAxVcc_UHHcCHDEQQudcGKAF6BAgbECw&sxsrf=ACQVn0-XIEogMp2cd_SshdN_dlCCdh23sg:1710647767330#htivrt=jobs&htidocid=3dyy4ZJFWqY6X_LZAAAAAA%3D%3D&fpstate=tldetail
"""
driver.get(url)
driver.maximize_window()


df = {
    "role": [],
    "company": [],
    "location": [],
    "link": [],
    # "posted": [],
    # "salary": [],
    # "type": [],
    "metadata": [],
    "description": []
}
cols = list(df.keys())


text = driver.page_source
html = HTMLParser(text)

job_block = html.css_first("div[class~='pE8vnd']")

print(job_block.css_first("h2.SBkjJd").text(deep=True, separator=' ', strip=False))


buttons = driver.find_elements(
    "xpath",
    "//div[@role='button' and @class='Fol1qc']"
)
num_jobs = len(buttons)
print(num_jobs)
