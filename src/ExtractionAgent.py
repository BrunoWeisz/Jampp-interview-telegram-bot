
class ExtractionAgent:
    def __init__(this, aWriter):
        this.fileWriter = aWriter
        

    def extractFromBanks(this, indexes, atmData):
        if len(indexes) == 1:
            this.extractFrom(indexes[0], atmData, 1)
        elif len(indexes) == 2:
            this.extractFrom(indexes[0], atmData, 0.7)
            this.extractFrom(indexes[1], atmData, 0.3)
        elif len(indexes) == 3:
            this.extractFrom(indexes[0], atmData, 0.7)
            this.extractFrom(indexes[1], atmData, 0.2)
            this.extractFrom(indexes[2], atmData, 0.1)
            
    def extractFrom(this, anIndex, atmData, anAmount):
        field = atmData[anIndex][len(atmData[anIndex])-1]
        if float(field) >= 1:
            atmData[anIndex][len(atmData[anIndex])-1] = str(float(field) - anAmount)
            this.fileWriter.write(atmData)
    
  