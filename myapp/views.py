from django.shortcuts import render
from django.shortcuts import render_to_response
from myapp.models import geoname
from django.template import RequestContext
from django.http import HttpResponseRedirect
import googlemaps
from utils import *


def test(request):
	abc = geoname.objects.filter(elevation__gte = '5000')
	casinos = geoname.objects.filter(fcode = 'CSNO')
	beaches = geoname.objects.filter(fcode = 'BCH')
	#abc = geoname.objects.all()[:5]
	#return render_to_response('test.html', RequestContext(request,{'abc': abc}))
	gmaps = googlemaps.Client(key='AIzaSyBsJEndyJAEpoHsfYe2GQcaOP2GmwlEzrk')
	#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
	geocode_result = gmaps.reverse_geocode((40.73655,-114.04358))
	#geocode_result = gmaps.distance_matrix('Washington, DC, USA', 'New York, NY, USA')
	#geocode_result = gmaps.distance_matrix('40.73655,-114.04358', 'New York, NY, USA')
	dis = distance(40.7128,74.0059,38.9072,77.0369)
	xyz = casinos[0].latitude


	#SELECT * FROM myapp_geonameid WHERE geonameid = 6942409
	#SELECT * FROM myapp_geoname WHERE geonameid = 10338767


	c = []
	for x in casinos:
		for y in beaches:
			if distance (x.latitude, x.longitude, y.latitude, y.longitude) < 15:
				c.append((x.geonameid, x.name, y.geonameid, y.name))
			z = x.latitude
	#import pdb; pdb.set_trace()
	#casinos[0].latitude
	return render_to_response('test.html', {'c': c, 'z': z, 'xyz': xyz, 'dis': dis, 'casinos': casinos,'beaches': beaches, 'abc': abc, 'geocode_result': geocode_result})


from django.contrib.auth import authenticate, login


def hello(request):
    #username = request.POST['username']
    #password = request.POST['password']
	if request.method == 'POST':

		#username = "shahvaiz"
		#password = "germany"
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
	        	#return render_to_response('/test/')
				return HttpResponseRedirect ('/test/')
	    #    else:
	            # Return a 'disabled account' error message
		else:
			#return render_to_response('fail.html')
			abc = 1
			return render_to_response('login.html', RequestContext(request, {'abc':abc}))

	else:
		return render_to_response('login.html', RequestContext(request, {}))
