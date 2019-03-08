from django.contrib import admin
from django.urls import path, include
import introduce.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', introduce.views.home, name="home"),
    path('travel', introduce.views.travel, name="travel"),
    path('mycareer', introduce.views.mycareer, name="mycareer"),
    path('book', introduce.views.book, name="book",) 
]
