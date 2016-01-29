#!/usr/bin/python
# -*- coding: utf-8 -*-


from process.tasks import fetch_company

args = []
for i in range(200, 1000):
    arg = {
        "url": "http://www.lagou.com/gongsi/%s.html" % i,
        "save_file": "./data/%s.json" % i
    }
    args.append(arg)


t1 = fetch_company.delay(args)

args = []
for i in range(100, 200):
    arg = {
        "url": "http://www.lagou.com/gongsi/%s.html" % i,
        "save_file": "./data/%s.json" % i
    }
    args.append(arg)

t2 = fetch_company.delay(args)
