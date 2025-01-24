from django.urls import path
from django.urls import include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns




urlpatterns = [
    path('',views.api_root,name='api_root'),
    path('list/',views.movie_list.as_view(),name='movie_list'),
    path('list/<int:pk>/',views.movie_details.as_view(),name='movie_details'),
    path('stream/',views.stream_list.as_view(),name='stream_list'),
    path('stream/<int:pk>',views.stream_details.as_view(),name='stream_details'),
    # path('review/',views.movie_review.as_view(),name='movie_review'),
    # path('revsiew/<int:pk>/',views.review_details.as_view(),name='review_details')
    path('list/<int:pk>/review/',views.movie_review.as_view()),
    path('list/<int:pk>/review_create/',views.Review_create.as_view())
    
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
