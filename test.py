#!/usr/bin/python
# -*- coding: utf-8 -*-

args = [{
    "url": "http://www.lagou.com/gongsi/451.html",
    "save_file": "./data/451.json"
}]

from process.tasks import fetch_company

t = fetch_company.delay(args)