from app import app

from models import Location


@app.route("/compsloc/")
def companiy_loc():
    locations = Location.query.all()

    locs = []
    for loc in locations:
        locs.append({
            "lng": loc.longitude,
            "lat": loc.latitude
        })
    return str(locs)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)