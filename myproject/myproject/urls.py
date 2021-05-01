from django.contrib import admin
from django.urls import path
from main.views import form, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index.html"),
    path('form/', form, name="form.html"),
]
