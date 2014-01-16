# Create your views here.
from django.template.loader import get_template
from django.template import Context
from django.http import *
import json
from django.views.decorators.csrf import csrf_exempt

authors = {'author1' : 'Shawn', 'author2' : 'Andrew'}

# Homepage
def home(request):
	t = get_template('index.html')
	html = t.render(Context(authors))
	return HttpResponse(html)

@csrf_exempt
def searchResults(request):
	if request.method != 'POST':
		return HttpResponseBadRequest()

	response_data = {}
	results = []
	for i in range(4):
		results.append({ "type" : "home", "number": str(str(i)*10)})
	response_data["results"] = results
	return HttpResponse(json.dumps(response_data), content_type="application/json")


# POST request with route ID to get all GPS Coords
@csrf_exempt
def getAllGPSCoords(request):
	if request.method != 'POST':
		return HttpResponseBadRequest()
	#routeId = request.POST['routeId']

	response_data = {}
	response_data['lats'] = [1.23, 4.56, 7.89]
	response_data['longs'] = [7.89, 4.56, 1.23]
	return HttpResponse(json.dumps(response_data), content_type="application/json")
