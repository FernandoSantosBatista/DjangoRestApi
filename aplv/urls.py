from django.urls import path
from aplv import views 
 
urlpatterns = [ 
    path(r'register', views.aplv_list),
    path(r'register/<id>/', views.getbyid),
]