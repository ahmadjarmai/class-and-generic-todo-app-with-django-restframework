from django.urls import path
from . import views

urlpatterns =[
    #class based view urls
    #path('list/', views.TodoApiView.as_view(), name='list'),
    #path('detail/<int:pk>/', views.TodoDetail.as_view(), name='detail'),

    #generics view urls 
    path('list/', views.TodoListCreate.as_view(), name='list'),
    path('detail/<int:pk>/', views.TodoUdateRetriveDelete.as_view(), name='detail')
]
