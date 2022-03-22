import csv

with open('../files/cajeros-automaticos.csv', 'r') as csvWithoutCash:
    with open('../files/cajeros-automaticos-cash.csv', 'w') as csvWithCash:
        reader = csv.reader(csvWithoutCash, delimiter = '#')
        writer = csv.writer(csvWithCash, delimiter = '#')
        
        for row in reader:
            
            # print(row)
            # print('\n')

            if row[0] == 'id':
                row.append('extracciones')
                writer.writerow(row)
            else:
                row.append(100)
                writer.writerow(row)