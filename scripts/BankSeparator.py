import csv

with open('../files/cajeros-automaticos-cash.csv', 'r') as csvFull:
    with open('../files/cajeros-automaticos-link.csv', 'w') as csvLink:
        with open('../files/cajeros-automaticos-banelco.csv', 'w') as csvBanelco:
            reader = csv.reader(csvFull, delimiter = '#')
            writerLink = csv.writer(csvLink, delimiter = '#')
            writerBanelco = csv.writer(csvBanelco, delimiter = '#')
            for row in reader:

                if row[0] == 'id':
                    writerLink.writerow(row)
                    writerBanelco.writerow(row)
                print(row)
                bank = row[4]    
                if bank == 'LINK':
                    writerLink.writerow(row)
                elif bank == 'BANELCO':
                    writerBanelco.writerow(row)
