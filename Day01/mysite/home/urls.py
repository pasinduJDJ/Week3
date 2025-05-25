from django.urls import path
from . import views
from .views import about_view, home_view

urlpatterns = [
    path('', home_view,name = 'home'),
    path('about/',about_view,name='about'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail')
]