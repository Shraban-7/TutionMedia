from django.urls import path
from .views import TuitionPostCreateView, TuitionListView, TuitionDetailView, Home, search, load_cities,Feedback_view

urlpatterns = [
    path('create/', TuitionPostCreateView.as_view(), name='create_tuition'),
    path('list/', TuitionListView.as_view(), name='list_tuition'),
    path('detail/<int:pk>/', TuitionDetailView.as_view(), name='detail'),
    path('Contact/', Feedback_view.as_view(), name='contact'),
    path('search/', search, name='filter'),
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),
]
