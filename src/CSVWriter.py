import csv

class CSVWriter:
    def __init__(this, routeToCsv):
        this.path = routeToCsv
    
    
    def write(this,dataToWrite):
        with open(this.path, 'w') as fileToModify:
        
            writer = csv.writer(fileToModify, delimiter = '#')
            
            for row in dataToWrite:
                writer.writerow(row)

   
