from django.shortcuts import render,redirect 
from .tasks import printing


def index(request):
	printing()
	return render(request,"app/index.html")

def next_page(request):
	return render(request,"app/next.html")