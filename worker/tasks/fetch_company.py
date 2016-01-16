#!/usr/bin/python
# -*- coding: utf-8 -*-


import json

import requests
from bs4 import BeautifulSoup

from ..app import app
# from .. import config

@app.task(ignore_result=True)
def fetch(urls):
    for url in urls:
        try:
            html = requests.get(url).content
        except Exception as err:
            print "get %s error:" % url, err
        else:
            try:
                soup = BeautifulSoup(html, "html.parser")
                company_data = json.loads(
                    soup.find("script", {"id": "companyInfoData"}).string)
                with open("C:/Users/daniel/Desktop/www.html", "w") as f:
                    f.write(json.dumps(company_data, indent=2))
            except Exception as err:
                print err
        print "done:", url