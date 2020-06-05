from django.urls import path
from .views import *
urlpatterns = [
    path('index/', postIndex),
    path('detail/<int:id>', postDetail),
    path('create/', postCreate),
    path('delete/', postDelete),
    path('update/', postUpdate),
]
