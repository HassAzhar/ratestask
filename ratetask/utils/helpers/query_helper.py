from typing import List

# Appending 'or' statements to query from a list of items
# which are to be compared to a single attribute
# e.g. we have a whole lot of port codes in our final query
# this function automates the process of adding all of those
# codes using a for loop. Separated for reusability
def query_builder(query: str, attribute: str, list: List):
    if query[len(query) - 1] != " ":
        query += " "
    query_list = []
    for item in list:
        query_list.append(f"{attribute}='{item}'")
    query += " or ".join(query_list)
    return query
