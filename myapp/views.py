from django.shortcuts import render
from django.shortcuts import render_to_response
from myapp.models import geoname
from django.template import RequestContext
from django.http import HttpResponseRedirect


def test(request):
	abc = geoname.objects.filter(elevation__gte = '5000')
	#abc = geoname.objects.all()[:5]
	#return render_to_response('test.html', RequestContext(request,{'abc': abc}))
	return render_to_response('test.html', {'abc': abc})

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
