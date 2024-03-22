from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login',views.login_page, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout_user, name='logout'),
    path('addtodo', views.add_todo, name='add-todo'),
    path('delete/<str:pk>', views.delete_todo, name='delete-todo'),
    path('finish/<str:pk>', views.finish_todo, name='finish-todo')

]