# This is our applications URL's file that we made. In this file we created a path for each view function 
# We also imported the function name from the views file. 
from django.urls import path
from .views import indexPageView, aboutPageView, dataPageView, detailPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("about/", aboutPageView, name="about"),
    path("data/", dataPageView, name="data"),
    path("<int:id>/", detailPageView, name="detailPage"),
]
