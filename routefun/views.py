# Create your views here.
from django.template.loader import get_template
from django.template import Context
from django.http import *
import json
from django.views.decorators.csrf import csrf_exempt
from routefun.models import *

authors = {'author1' : 'Shawn', 'author2' : 'Andrew'}

# Homepage
def home(request):
	t = get_template('alternate.html')
	html = t.render(Context({}))#Context(authors))
	return HttpResponse(html)

@csrf_exempt
def searchResults(request):
	if request.method != 'POST':
		return HttpResponseBadRequest()

	if 'ranking' in request.POST:
		ranking = request.POST['ranking']
	else:
		ranking = 4
	# ranking = 4
	response_data = getTripsByRanking(ranking)
	print "search results"
	print response_data
	return HttpResponse(json.dumps(response_data), content_type="application/json")


# POST request with route ID to get all GPS Coords
@csrf_exempt
def getAllGPSCoords(request):
	# if request.method != 'POST':
	# 	return HttpResponseBadRequest()
	#routeId = request.POST['routeId']
	print "allgps"

	if request.method != 'POST':
		return HttpResponseBadRequest()

	if 'idTrips' in request.POST and 'idVehicles' in request.POST:
		idTrips = request.POST['idTrips']
		idVehicles = request.POST['idVehicles']
	else:
		idTrips = 5
		idVehicles = 2

	response_data = getAllGPSCoordsByTrip(idTrips, idVehicles)
	# print response_data
	return HttpResponse(json.dumps(response_data), content_type="application/json")