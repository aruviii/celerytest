from django.urls import path 
from .views import index , next_page

urlpatterns = [
	path("index/",index,name="index"),
	path("next/",next_page,name="next"),
]
