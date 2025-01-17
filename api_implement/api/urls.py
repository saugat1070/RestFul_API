from django.urls import path
from django.urls import include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns




urlpatterns = [
    path('',views.api_root,name='api_root'),
    path('list/',views.movie_list.as_view(),name='movie_list'),
    path('list/<int:pk>',views.movie_details.as_view(),name='movie_details'),
    path('stream/',views.stream_list.as_view(),name='stream_list'),
    path('stream/<int:pk>',views.stream_details.as_view(),name='stream_details'),
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
