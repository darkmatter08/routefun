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
		results.append({ "type" : "Enthusiast", "number": str(5)})
	response_data["results"] = results
	return HttpResponse(json.dumps(response_data), content_type="application/json")


# POST request with route ID to get all GPS Coords
@csrf_exempt
def getAllGPSCoords(request):
	# if request.method != 'POST':
	# 	return HttpResponseBadRequest()
	#routeId = request.POST['routeId']
	print "allgps"
	response_data = {}
	response_data['lats'] = lats
	response_data['longs'] = longs
	return HttpResponse(json.dumps(response_data), content_type="application/json")

lats = [
-83.30556616,
-83.30556616,
-83.30556616,
-83.30556616,
-83.30556616,
-83.30556616,
-83.3072327,
-83.30728983,
-83.30728983,
-83.30728983,
-83.30728983,
-83.30728983,
-83.30728983,
-83.30728983,
-83.30728983,
-83.30746556,
-83.30750789,
-83.30753858,
-83.30754438,
-83.30758745,
-83.30761816,
-83.30761948,
-83.30764121,
-83.30763465,
-83.30764416,
-83.30764598,
-83.30764663,
-83.30764677,
-83.30764677,
-83.30764677,
-83.30764677,
-83.30764677,
-83.30764677,
-83.30764677,
-83.30764677,
-83.30764677,
-83.30764677,
-83.30764677,
-83.30764677,
-83.30764677,
-83.30764677,
-83.30764677,
-83.30764878,
-83.30764885,
-83.30764912,
-83.30764912,
-83.30764846,
-83.30764846,
-83.30764846,
-83.3076507,
-83.30764931,
-83.30765259,
-83.30765598,
-83.30765481,
-83.30808194,
-83.30807319,
-83.30810658,
-83.30809174,
-83.30807391,
-83.30807202,
-83.3080778,
-83.30807108,
-83.30805157,
-83.30796542,
-83.30791559,
-83.30787077,
-83.30785871,
-83.30788604,
-83.3080066,
-83.30801247,
-83.30801221,
-83.30800507,
-83.30800839,
-83.30801004,
-83.30801011,
-83.30802289,
-83.30802804,
-83.30803185,
-83.30804148,
-83.30804609,
-83.30804956,
-83.30804922,
-83.30805069,
-83.30805091,
-83.3080551,
-83.30805614,
-83.30805529,
-83.30805541,
-83.30805548,
-83.30805545,
-83.30805554,
-83.30805573,
-83.30805567,
-83.30805594,
-83.30805737,
-83.30807396,
-83.30812719,
-83.30832917,
-83.30846749,
-83.30858292,
-83.30873372,
-83.30886343,
-83.3089927,
-83.30913243,
-83.30925816,
-83.30943414,
-83.30957061,
-83.30981966,
-83.3100447,
-83.31024264,
-83.31042034,
-83.31063868,
-83.3108433,
-83.31103211,
-83.3111921,
-83.31137959,
-83.31159978,
-83.31179135,
-83.3120198,
-83.31225722,
-83.31246943,
-83.31266397,
-83.31285847,
-83.31304436,
-83.31325079,
-83.31348314,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31982188,
-83.31998117,
-83.31998117,
-83.31998117,
-83.31998117,
-83.31998117,
-83.31998117,
-83.31998117,
-83.32142327,
-83.32158538,
-83.32178505,
-83.32194066,
-83.32210048,
-83.32246225,
-83.32267199,
-83.32290918,
-83.32290918,
-83.32290918,
-83.32290918,
-83.32290918,
-83.32290918,
-83.32290918,
-83.32290918,
-83.32290918,
-83.32290918,
-83.32492025,
-83.32515007,
-83.32537471,
-83.32560649,
-83.32578958,
-83.32602072,
-83.32623847,
-83.32645975,
-83.3266954,
-83.32691517,
-83.32708107,
-83.32737075,
-83.32760569,
-83.32788603,
-83.32811016,
-83.32833201,
-83.32854096,
-83.32872942,
-83.32894459,
-83.32915881,
-83.32915881,
-83.32915881,
-83.32915881,
-83.3299175,
-83.3300788,
-83.33022525,
-83.33029646,
-83.3302901,
-83.33039193,
-83.3304577,
-83.33055779,
-83.33065933,
-83.33074143,
-83.3307455,
-83.3308288,
-83.33080487,
-83.3308634,
-83.3308634,
-83.33098729,
-83.33104636,
-83.33116361,
-83.33127225,
-83.33148728,
-83.33162144,
-83.33181392,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
]

longs = [
-83.31024264,
-83.31042034,
-83.31063868,
-83.3108433,
-83.31103211,
-83.3111921,
-83.31137959,
-83.31159978,
-83.31179135,
-83.3120198,
-83.31225722,
-83.31246943,
-83.31266397,
-83.31285847,
-83.31304436,
-83.31325079,
-83.31348314,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31369293,
-83.31982188,
-83.31998117,
-83.31998117,
-83.31998117,
-83.31998117,
-83.31998117,
-83.31998117,
-83.31998117,
-83.32142327,
-83.32158538,
-83.32178505,
-83.32194066,
-83.32210048,
-83.32246225,
-83.32267199,
-83.32290918,
-83.32290918,
-83.32290918,
-83.32290918,
-83.32290918,
-83.32290918,
-83.32290918,
-83.32290918,
-83.32290918,
-83.32290918,
-83.32492025,
-83.32515007,
-83.32537471,
-83.32560649,
-83.32578958,
-83.32602072,
-83.32623847,
-83.32645975,
-83.3266954,
-83.32691517,
-83.32708107,
-83.32737075,
-83.32760569,
-83.32788603,
-83.32811016,
-83.32833201,
-83.32854096,
-83.32872942,
-83.32894459,
-83.32915881,
-83.32915881,
-83.32915881,
-83.32915881,
-83.3299175,
-83.3300788,
-83.33022525,
-83.33029646,
-83.3302901,
-83.33039193,
-83.3304577,
-83.33055779,
-83.33065933,
-83.33074143,
-83.3307455,
-83.3308288,
-83.33080487,
-83.3308634,
-83.3308634,
-83.33098729,
-83.33104636,
-83.33116361,
-83.33127225,
-83.33148728,
-83.33162144,
-83.33181392,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
-83.33196569,
]