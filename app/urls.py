from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.myapi.as_view()),
    path('admin/', admin.site.urls),
]
