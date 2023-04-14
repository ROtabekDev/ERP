from django.urls import path

from apps.internship.api_endpoints import intern, direction

urlpatterns = [
    # intern
    path('intern/create/', intern.InternCreateAPIView.as_view(), name='intern-create'),
    path('intern/list/', intern.InternListAPIView.as_view(), name='intern-list'),
    path('intern/detail/<int:pk>/', intern.InternDetailAPIView.as_view(), name='intern-detail'),
    path('intern/update/<int:pk>/', intern.InternUpdateAPIView.as_view(), name='intern-update'),
    path('intern/delete/<int:pk>/', intern.InternDestroyAPIView.as_view(), name='intern-delete'),

    # direction
    path('direction/list/', direction.DirectionListAPIView.as_view(), name='direction-list'),
]