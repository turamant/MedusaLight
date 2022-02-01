from django.urls import path

from rest_api.views import GetListAllNew

app_name = 'web_admin'

urlpatterns = [
    path('list/all/new/', GetListAllNew.as_view())
]