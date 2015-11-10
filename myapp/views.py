from django.shortcuts import render
from django.shortcuts import render_to_response
from myapp.models import geoname


def test(request):
	abc = geoname.objects.filter(elevation__gte = '5000')
	#abc = geoname.objects.all()[:5]
	return render_to_response('test.html', {'abc': abc})

