from src.CSVReader import CSVReader
from src.CSVWriter import CSVWriter

class ExtractionRestorer:
    def restoreExtractions(this, pathToCsv):
        print('starting restauration')
        data = CSVReader(pathToCsv).retrieveInformation()
        map(lambda row : row[0:-1] + ["100"],
            data)
        CSVWriter(pathToCsv).write(data)
        print('ending restauration')
