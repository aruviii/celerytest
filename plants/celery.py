
import os 
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plants.settings')

app = Celery('plants_projects')

app.config_from_object('django.conf:settings',namespace = 'CELERY')


app.conf.beat_schedule = {
	'printing_2s' : {
		'task':"app.tasks.printing",
		'schedule' : 2.0
	}
}


app.autodiscover_tasks()