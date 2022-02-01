from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_admin.urls', namespace='web_admin')),
    path('api/v1/new/', include('rest_api.urls', namespace='rest_api'))

]