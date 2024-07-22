from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from library.api import app
from django.http import HttpResponse

api = NinjaAPI()

#Message displayed as soon as the project is run
def home(request):
    return HttpResponse("Welcome to the Online Library Management System")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', app.urls),
    path('', home),
]
