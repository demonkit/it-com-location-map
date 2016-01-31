#!/usr/bin/python
# -*- coding: utf-8 -*-


from display import app
from display.models import Company, Location


@app.route("/companies")
def company_list():
    companies = Company.query.all()
    print companies
    return
