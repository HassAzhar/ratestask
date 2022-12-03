from typing import List

def query_builder(query: str, attribute: str, list: List):
    if query[len(query) - 1] != ' ':
        query += ' '
    query_list = []
    for item in list:
        query_list.append(f'{attribute}=\'{item}\'')
    query += ' or '.join(query_list)
    return query