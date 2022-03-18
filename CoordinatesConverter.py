from geopy import distance

class CoordinatesToMeters:
    def distanceInMeters(this, long1, lat1, long2, lat2):
        originCoordinates = (lat1, long1)
        destinationCoordinates = (lat2, long2)
        return distance.distance(originCoordinates, destinationCoordinates).km * 1000