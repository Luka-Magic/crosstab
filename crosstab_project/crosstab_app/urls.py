from django.urls import URLPattern, path
from . import views

app_name = 'crosstab_app'
urlpatterns = [
    path('', views.index)
]
