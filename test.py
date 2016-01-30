#!/usr/bin/python
# -*- coding: utf-8 -*-


from process.tasks import fetch_company

args = []
for i in range(2000, 3000):
    arg = {
        "url": "http://www.lagou.com/gongsi/%s.html" % i,
        "save_file": "./data/%s.json" % i
    }
    args.append(arg)


t1 = fetch_company.delay(args)

args = []
for i in range(1000, 2000):
    arg = {
        "url": "http://www.lagou.com/gongsi/%s.html" % i,
        "save_file": "./data/%s.json" % i
    }
    args.append(arg)

t2 = fetch_company.delay(args)

# 2016-01-30 14:14 done with 2999