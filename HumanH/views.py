from django.shortcuts import render
from django.http import HttpResponse
from django.template  import loader
from .models import Tutorial as T

from .HumanHForm import HumanHForm 
# Create your views here.
def homePage(request):
	list1 = T.objects.all();
	lists = {
		"hi":"this is number 1",
		"hw":"this is number 2",
		"he":T.objects.all(),
	}
	return render(request,'HumanH/home.html',lists)
def aboutPage(request):
	return render(request,'HumanH/about.html',{})
def createPage(request):
	form = HumanHForm(request.POST or None)
	if form.is_valid():
		form.save()

	lists = {'form': form}
	return render(request,'HumanH/create.html',lists)
def deletePage(request):
	return render(request,'HumanH/delete.html',{})
def showPage(request):
	return render(request,'HumanH/show.html',{})
