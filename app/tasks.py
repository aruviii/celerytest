import time
from django.shortcuts import render,redirect 

from celery import shared_task

@shared_task
def printing():
	time.sleep(10)
	return redirect("next")
