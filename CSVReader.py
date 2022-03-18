from csv import reader

class CSVReader:
    def __init__(this, routeToCsv):
        
        this.atmInformation = []

        with open(routeToCsv, 'r') as readObj:
            csvReader = reader(readObj, delimiter = '#')
            for row in csvReader:
                this.atmInformation.append(row)

    def retrieveInformation(this):
        return this.atmInformation
    