from django.shortcuts import render

# Create your views here.

def index(request):
	# "the homepage of the webapp"
	return render(request,'learning_logs/index.html')
	

