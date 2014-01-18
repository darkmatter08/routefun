#from django.db import models
#from django.db import connection
from django.db import connections

# Create your models here.
# class OBD_Trips_enh:
#   idVehicle = models.AutoField(primary_key=True)
#   idTrip = models.AutoField(primary_key=True)
#   ranking = models.DecimalField

# class OBD_CarData:
#   idData = 
#   idVehicle = models.Model(primary_key=true)
#   lat = models.Model()
#   lon = models.Model()

# Gets all trips with ranking >= ranking (in the db)
def getTripsByRanking(ranking):
	cursor = connections['db7x'].cursor()
	cursor.execute("select a.idTrips, a.idVehicles from OBD_Trips_enh a where a.ranking > %s", [ranking])
	desc = cursor.description
	return [
		dict(zip([col[0] for col in desc], row))
		for row in castLongToInt(cursor.fetchall())
	]

# Return a dict in the form {"lats": [], "longs": []} with
# all gps coords from the trip identified by idTrips, idVehicles
def getAllGPSCoordsByTrip(idTrips, idVehicles):
	cursor = connections['db7x'].cursor()
	cursor.execute("select Latitude, Longitude from OBD_CarData where idTrips = %s and idVehicles = %s", [idTrips, idVehicles])
	desc = cursor.description
	return [
		dict(zip([col[0] for col in desc], row))
		for row in cursor.fetchall()
	]

def cleanTrailingLs(dbData):
	result = []
	for (lat, lon) in dbData:
		newLat = lat
		newLon = lon
		if lat.endswith('L'):
			newlat = lat[:len(lat)-1] 
		if lon.endswith('L'):
			newlon = lon[:len(lon)-1]
		result.append((newLat, newLon))
	return result

def castLongToInt(dbData):
	result = []
	for (first, second) in dbData:
		result.append((int(first), int(second)))
	return result