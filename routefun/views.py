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

# POST with ranking to get all routes with route.ranking >= ranking
@csrf_exempt
def searchResults(request):
	if request.method != 'POST':
		return HttpResponseBadRequest()

	if 'ranking' in request.POST:
		ranking = request.POST['ranking']
	else:
		return HttpResponseBadRequest()

	response_data = getTripsByRanking(ranking)
	return HttpResponse(json.dumps(response_data), content_type="application/json")


# POST with idTrips, idVehicles to get all GPS Coords
@csrf_exempt
def getAllGPSCoords(request):
	if request.method != 'POST':
		return HttpResponseBadRequest()

	if 'idTrips' in request.POST and 'idVehicles' in request.POST:
		idTrips = request.POST['idTrips']
		idVehicles = request.POST['idVehicles']
	else:
		return HttpResponseBadRequest()

	response_data = getAllGPSCoordsByTrip(idTrips, idVehicles)
	return HttpResponse(json.dumps(response_data), content_type="application/json")
