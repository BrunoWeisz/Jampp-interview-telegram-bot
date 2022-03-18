import numpy as np
from scipy.spatial import KDTree
from CoordinatesConverter import CoordinatesToMeters

class ATMNodeOrdering:
    def __init__(this, csvReader):

        rows = csvReader.retrieveInformation()

        this.atmPositions = []
        this.atmData = []

        for row in rows:
            if not row[1] == 'long':
                this.atmPositions.append([float(row[1]), float(row[2])])
                this.atmData.append([row[3], row[5]])

        this.atmPositionKDTree = KDTree(this.atmPositions)

    def closestNodes(this, long, lat):
        d, index = this.atmPositionKDTree.query(x = [long,lat], k = 3)
        inRangeATMData = []
        for i in range(3):
            if CoordinatesToMeters().distanceInMeters(d[i],0,0,0) < 500:
                inRangeATMData.append(this.atmData[index[i]] + this.atmPositions[index[i]])

        return inRangeATMData
