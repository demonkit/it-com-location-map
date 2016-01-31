#!/usr/bin/python
# -*- coding: utf-8 -*-


from display.databases import db


class Company(db.Model):
    __tablename__ = 'company'

    cid = db.Column(db.Integer, unique=True)
    logo = db.Column(db.String())
    name = db.Column(db.String())
    short_name = db.Column(db.String())
    url= db.Column(db.String())
    industry_field = db.Column(db.String())
    size = db.Column(db.String())
    city= db.Column(db.String())
    finance_stage = db.Column(db.String())


class Location(db.Model):
    __tablename__ = 'location'

    company_id = db.Column(db.Integer, foreign_key="Company.cid")
    brief_position = db.Column(db.String())
    detail_position = db.Column(db.String())
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
