# Finding route information on bus rides

import csv
from collections import Counter

file = 'Data/ctabus.csv'

def read_as_dict(): 

    information = []

    with open(file) as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows: 
            current_route = {
                header[x]: row[x] for x in range(len(row))
            }

            information.append(current_route)
        return information


def total_rides_on_each_route(file_as_list_of_dicts): 
    count = Counter()
    for x in file_as_list_of_dicts: 
        count[x['route']] += int(x['rides'])
    print(count)



if __name__ == "__main__": 
    information_dict = read_as_dict()
    total_rides_on_each_route(information_dict)