from django.urls import path
from . import views

app_name = 'ipl_app'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("extra_runs", views.extra_runs, name="extra_runs"),

]
