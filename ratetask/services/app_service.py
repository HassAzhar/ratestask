from ratetask.db import db
from typing import List
from ratetask.utils.helpers.query_helper import query_builder
from datetime import datetime

def get_regions(region: str):  
    regions = [region]
    iterator = 0
    while iterator < len(regions):
        regions += db.fetch_formatted(f'select slug from regions where parent_slug=\'{regions[iterator]}\';')
        iterator += 1
    return regions

def get_ports(regions: List[str]):
    query = 'select code from ports where '
    query = query_builder(query, 'parent_slug', regions)
    query += ';'
    return db.fetch_formatted(query)

def check_if_port(region: str):
    return len(db.fetch_formatted(f'select code from ports where code=\'{region}\'')) == 1

def fetch_aggregates(date_from: str, date_to: str, origin_ports: List[str], destination_ports: List[str]):
    query = f'select day, avg(price), count(price) from prices where day between \'{date_from}\' and \'{date_to}\' and ('
    query = query_builder(query, 'orig_code', origin_ports)
    query += ') and ('
    query = query_builder(query, 'dest_code', destination_ports)
    query += ') group by day;'
    return db.fetch_execute(query)
    
def format_rates(result):
    formatted_result = []
    for item in result:
        json_obj = {}
        json_obj['date'] = datetime.strftime(item[0], '%Y-%m-%d')
        if item[2] < 3:
            json_obj['average_price'] = None
        else:
            json_obj['average_price'] = int(item[1])
        formatted_result.append(json_obj)
    return formatted_result
    

def agregate_rates(date_from: str, date_to: str, origin: str, destination: str):
    is_origin_port = check_if_port(origin)
    is_dest_port = check_if_port(destination)
    origin_ports = [origin]
    if not is_origin_port:
        origin_regions = get_regions(origin)
        origin_ports = get_ports(origin_regions)
    
    destination_ports = [destination]
    if not is_dest_port:
        destination_regions = get_regions(destination)
        destination_ports = get_ports(destination_regions)
    
    result = fetch_aggregates(date_from, date_to, origin_ports, destination_ports)
    formatted_result = format_rates(result)

    return formatted_result
    #db.fetch_execute(f'select * from prices where day between \'{date_from}\' and \'{date_to}\'')