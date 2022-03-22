import numpy as np
from scipy.spatial import KDTree
from src.CoordinatesConverter import CoordinatesToMeters

class ATMNodeOrdering:
    def __init__(this, csvReader):
        this.atmData = csvReader.retrieveInformation()
        this.atmPositions = []

        for row in this.atmData: #emprolijar
            if not row[1] == 'long':
                this.atmPositions.append([float(row[1]), float(row[2])])

        this.atmPositionKDTree = KDTree(this.atmPositions)

    def closestNodes(this, long, lat):
        d, index = this.atmPositionKDTree.query(x = [long,lat], k = 3)
        inRangeATMIndexes = []

        for i in range(3):
            if CoordinatesToMeters().distanceInMeters(d[i],0,0,0) < 500:
                inRangeATMIndexes.append(index[i])

        return inRangeATMIndexes, this.atmData
