from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from .views import *

app_name = 'Core'

urlpatterns = [
	path('', home, name='home'),
	 path('ajax/button_clicked/', csrf_exempt(button_clicked), name='button_clicked'),

]