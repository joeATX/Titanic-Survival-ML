# default present
from django.contrib import admin
from django.urls import path

# add this to import our views file
from Titanic_Survial_Prediction_Web import views

urlpatterns = [
    path('admin/', admin.site.urls),

     # add these to configure our home page (default view) and result web page
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
]
