# import path
from django.urls import path

from . import views
urlpatterns = [
    # "" : is the URL that the client has to visit and views.index : is the result that we have to display when client visit URL
    path("", views.index, name="index"),
    #path("brian", views.brian, name='brian'),
    #path("david", views.david, name='david')

    # Introduction to the url with placeholders in order to comment brian and david function
    path("<str:name>", views.greet, name="greet")

]