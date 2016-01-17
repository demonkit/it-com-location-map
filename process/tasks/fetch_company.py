#!/usr/bin/python
# -*- coding: utf-8 -*-


from gevent import monkey
monkey.patch_all()

import json

import requests
from bs4 import BeautifulSoup
from celery.utils.log import get_task_logger

from process.app import app
from process import exceptions
# from .. import config


logger = get_task_logger(__name__)


@app.task(ignore_result=True)
def fetch(args):
    for item in args:
        url = item['url']
        save_file = item['save_file']
        try:
            resp = requests.get(url)
            if resp.status_code != 200:
                raise exceptions.HttpError("got unexpected status code")
            html = resp.content
        except exceptions.HttpError:
            logger.info("get %s code for url: %s",
                        resp.status_code,
                        url)
        except Exception as err:
            logger.error("fetching url %s error: %s",
                         url, err)
        else:
            try:
                soup = BeautifulSoup(html, "html.parser")
                company_data = json.loads(
                    soup.find("script", {"id": "companyInfoData"}).string)
                with open(save_file, "w") as f:
                    f.write(json.dumps(company_data, indent=2))
            except Exception as err:
                logger.error("get json from url %s error: %s",
                             url, err)
        logger.info("fetching url %s done", url)
