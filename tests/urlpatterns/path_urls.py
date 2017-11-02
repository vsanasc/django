from django.conf.urls import include
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('articles/2003/', views.empty_view, name='articles-2003'),
    path('articles/<int:year>/', views.empty_view, name='articles-year'),
    path('articles/<int:year>/<int:month>/', views.empty_view, name='articles-year-month'),
    path('articles/<int:year>/<int:month>/<int:day>/', views.empty_view, name='articles-year-month-day'),
    path('users/', views.empty_view, name='users'),
    path('users/<id>/', views.empty_view, name='user-with-id'),
    path('included_urls/', include('urlpatterns.included_urls')),
    re_path(r'^regex/(?P<pk>[0-9]+)/$', views.empty_view, name='regex'),
    path('', include('urlpatterns.more_urls')),
    path('<lang>/<path:url>/', views.empty_view, name='lang-and-path'),
]
