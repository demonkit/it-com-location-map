#!/usr/bin/python
# -*- coding: utf-8 -*-


from app import app
from models import Company, Location


@app.route("/compsloc/")
def companiy_loc():
    locations = Location.query.all()

    locs = []
    for loc in locations:
        locs.append({
            "lng": loc.longitude,
            "lat": loc.latitude
        })
    return locs


@app.route("/companies")
def company_list():
    companies = Company.query.all()
    print companies
    return
