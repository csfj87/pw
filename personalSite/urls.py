from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepg, name='homepg'),
    path('post/<str:pk>', views.post, name='post'),
    path('blog', views.blog, name='blog'),
    path('resume', views.resumepg, name='resumepg'),
    path('/', views.subscription, name="subscription"),
    # path('home', views.message, name='message')
]