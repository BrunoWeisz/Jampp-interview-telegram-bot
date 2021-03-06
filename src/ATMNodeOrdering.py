from scipy.spatial import KDTree
from src.CoordinatesConverter import CoordinatesToMeters

class ATMNodeOrdering:
    def __init__(this, csvReader):
        this.atmData = csvReader.retrieveInformation()[1:-1]
        this.atmPositions = list(map(lambda row : [float(row[1]), float(row[2])], this.atmData))
        this.atmPositionKDTree = KDTree(this.atmPositions)
        

    def closestNodes(this, long, lat):
        d, index = this.atmPositionKDTree.query(x = [long,lat], k = 3)


        inRangeATMIndexes = []
        for i in range(3):
            if CoordinatesToMeters().distanceInMeters(d[i],0,0,0) < 700:
                inRangeATMIndexes.append(index[i])

        return inRangeATMIndexes, this.atmData
