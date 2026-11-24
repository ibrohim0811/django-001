from django.contrib import admin
from django.urls import path

from app.views import book_detail, book_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_list),
    path('book-detail/<int:pk>', book_detail, name="book-detail"),
]
