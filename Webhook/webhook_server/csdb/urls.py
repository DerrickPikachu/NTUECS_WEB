from django.urls import path
from . import views

app_name = 'csdb'
urlpatterns = [
    path('<int:test>', views.testView),
]

