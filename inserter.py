import sys

sys.path.append('/Users/famousforrest/workspace/crime/crime')

from django.core.management import setup_environ
import settings
setup_environ(settings)


# app settings
from crimes.models import Crime

from datetime import datetime
from dateutil import parser
import csv
import json
import requests
from decimal import *

#API_ENDPOINT = 'http://data.cityofchicago.org/api/views/hx8q-mf9v/rows.json'

def insert_crime_csv(file_name):
    f = open(file_name, 'rU')
    reader = csv.DictReader(f)

    for row in reader:
        insert_row(row)

def insert_row(row):
    if row['ARREST'] == 'Y':
      arrest = True
    else:
      arrest = False
    if row['DOMESTIC'] == 'Y':
      domestic = True
    else:
      domestic = False
    date = parser.parse(row['DATE  OF OCCURRENCE'])
    ward = row['WARD']
    x_cd = row['X COORDINATE']
    y_cd = row['Y COORDINATE']
    latitude = row['LATITUDE']
    longitude = row['LONGITUDE']
    if ward:
      ward = int(ward)
    else:
      ward = None
    if x_cd:
      x_cd = int(x_cd)
    else:
      x_cd = None
    if y_cd:
      y_cd = int(y_cd)
    else:
      y_cd = None
    if latitude:
      latitude = Decimal(latitude)
    else:
      latitude = None
    if longitude:
      longitude = Decimal(longitude)
    else:
      longitude = None

    c = Crime(
        description=row[' SECONDARY DESCRIPTION'],
        fbi_code=row['FBI CD'],
        location_type=row[' LOCATION DESCRIPTION'],
        beat=row['BEAT'],
        case_num =row['CASE#'],
        date = date,
        block = row['BLOCK'],
        iucr = row[' IUCR'],
        crime_type = row[' PRIMARY DESCRIPTION'],
        arrest = arrest,
        domestic = domestic,
        ward = ward,
        x_cd = x_cd,
        y_cd = y_cd,
        year = 2012,
        latitude = latitude,
        longitude = longitude,
        updated_on = datetime.now()
        )
    print c, c.latitude, c.longitude
    c.save()


insert_crime_csv('../chicago_crime_2012.csv')

# def get_all_crimes(view_id):
#     API_ENDPOINT = 'http://data.cityofchicago.org/api/views/%s/rows.json' % view_id
#     reps = requests.get(API_ENDPOINT).content
#     parsed_json = 
