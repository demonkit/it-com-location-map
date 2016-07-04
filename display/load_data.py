
import json
import os

import config
from app import db
from models import Company, Location


DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)
)), "data")

EXT = "json"


class Loader(object):

    def __init__(self, data_dir):
        self.data_dir = data_dir

    def traverse(self):
        for filename in os.listdir(self.data_dir):
            split = filename.split(".")
            if len(split) > 1 and split[-1] == EXT:
                yield os.path.join(self.data_dir, filename)

    def run(self):
        def save_obj(data):
            company = Company(
                cid=data['companyId'],
                logo=config.Static.LAGOU_WEBSITE + "/"
                     + data['coreInfo']['logo'],
                name=data['coreInfo']['companyName'],
                short_name=data['coreInfo']['companyShortName'],
                url=data['coreInfo']['companyUrl'],
                industry_field=data['baseInfo']['industryField'],
                size=data['baseInfo']['companySize'],
                city=data['baseInfo']['city'],
                finance_stage=data['baseInfo']['financeStage']
            )
            db.session.add(company)
            locations = []
            for item in data['location']:
                loc = Location(
                    company_id=data['companyId'],
                    brief_position=item['briefPosition'],
                    detail_position=item['detailPosition'],
                    longitude=item.get('longitude', ""),
                    latitude=item.get('latitude', "")
                )
                locations.append(loc)
            if locations:
                db.session.bulk_save_objects(locations)

        for path in self.traverse():
            with open(path) as f:
                try:
                    data = json.loads(f.read())
                    save_obj(data)
                except Exception, exp:
                    print "load %s encounters error %s" % (path, str(exp))
        db.session.commit()


if __name__ == '__main__':
    loader = Loader(DATA_DIR)
    loader.run()
