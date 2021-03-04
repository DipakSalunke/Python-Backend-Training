from django.urls import path

from . import views
app_name = "ninjas"
urlpatterns = [
    path('', views.IndexList.as_view(), name='index'),
    path('<int:dev_id>/', views.DetailsList.as_view(), name='details'),
    path('<str:skill>/', views.DevelopersList.as_view(), name='developers'),
    path('<int:dev_id>/level/', views.level, name='level'),
]