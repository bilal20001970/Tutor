from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.loginPage, name="logout"),
    path('register/', views.register, name="register"),
    path('upload/', views.upload_video, name="upload"),
    path('view/<str:pk>/', views.video_view, name='view')

]