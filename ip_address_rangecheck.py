import sys
from ipaddress import ip_network
import csv

with open(sys.argv[1], newline='') as csv1:
    reader = csv.reader(csv1)
    csv1_set = set()
    for row in reader:
        try:
            row_set = {int(host) for host in list(ip_network(row[1]).hosts())}
        except ValueError:
            print('cannot parse: ', row[1])
            continue
        csv1_set = csv1_set | row_set

with open(sys.argv[2], newline='') as csv2, open(sys.argv[3], 'w', newline='') as result:
    reader = csv.reader(csv2)
    writer = csv.writer(result)
    for row in reader:
        try:
            row_set = {int(host) for host in list(ip_network(row[1]).hosts())}
        except ValueError:
            print('cannot parse: ', row[1])
            row.append('cannot parse')
            writer.writerow(row)
            continue
        if(row_set <= csv1_set):
            row.append('included')
        else:
            row.append('not included')
        writer.writerow(row)
