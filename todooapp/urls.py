from django.urls import path
from .import views

urlpatterns = [

    path('',views.task,name='task'),
    # path('details/',views.details,name='details'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('classhome/', views.TaskListview.as_view(), name='classhome'),
    path('classdetail/<int:pk>/', views.TaskDetailview.as_view(), name='classdetail'),
    path('classupdate/<int:pk>/', views.TaskUpdateview.as_view(), name='classupdate'),
    path('classdelete/<int:pk>/', views.TaskDeleteview.as_view(), name='classdelete'),
]
