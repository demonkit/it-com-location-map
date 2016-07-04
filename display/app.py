

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from models import Location


app = Flask(__name__)
app.config.from_object("config.Config")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#
# @app.route("/companies")
# def company_list():
#     companies = Company.query.all()
#     print companies
#     return


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
