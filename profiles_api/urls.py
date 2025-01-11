from django.urls import path

from profiles_api import views
# from profiles_project.urls import urlpatterns

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]