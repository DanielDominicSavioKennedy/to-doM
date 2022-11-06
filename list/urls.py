from django.urls import path
from list import views

urlpatterns = [

path("",views.index,name="home"), 
path('delete/<list_id>',views.delete,name='delete'),  
path('complete/<list_id>',views.complete,name='complete'),
path('incomplete/<list_id>',views.incomplete,name='incomplete'),
path('edit/<list_id>',views.edit,name="edit"),
]
