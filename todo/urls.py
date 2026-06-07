
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.task_list, name= 'task_list'),
    path('add/',views.add_task,name='add_task'),
    path('update/<int:id>/',views.update_task,name='update_task'),
    path('delete/<int:id>/',views.delete_task,name='delete_task'),
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]