#!/usr/bin/python
# -*- coding: utf-8 -*-


from app import db


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer, unique=True)
    logo = db.Column(db.String(127))
    name = db.Column(db.String(127))
    short_name = db.Column(db.String(127))
    url= db.Column(db.String(127))
    industry_field = db.Column(db.String(127))
    size = db.Column(db.String(127))
    city= db.Column(db.String(127))
    finance_stage = db.Column(db.String(127))


class Location(db.Model):
    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer)#, foreign_key="Company.cid")
    brief_position = db.Column(db.String(127))
    detail_position = db.Column(db.String(127))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)


# db.create_all()
