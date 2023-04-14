from django.urls import path

from .api_endpoints import event

urlpatterns = [
    path('create/', event.EventCreateAPIView.as_view(), name='event-create'),
    path('list/', event.EventListAPIView.as_view(), name='event-list'),
    path('detail/<int:pk>/', event.EventDetailAPIView.as_view(), name='event-detail'),
    path('update/<int:pk>/', event.EventUpdateAPIView.as_view(), name='event-update'),
    path('delete/<int:pk>/', event.EventDestroyAPIView.as_view(), name='event-delete'),
]