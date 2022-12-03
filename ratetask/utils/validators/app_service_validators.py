from voluptuous import Schema
from datetime import datetime

def date_validator(fmt='%Y-%m-%d'):
    return lambda v: datetime.strptime(v, fmt)

rates_validator = Schema({'date_from' : date_validator(), 'date_to': date_validator(), 'origin': str, 'destination': str})