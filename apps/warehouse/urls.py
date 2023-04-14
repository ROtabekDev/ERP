from django.urls import path

from .api_endpoints import equipment, equipment_name, equipment_category

urlpatterns = [
    # equipment
    path('equipment/create/', equipment.EquipmentCreateAPIView.as_view(), name='equipment-create'),
    path('equipment/list/', equipment.EquipmentListAPIView.as_view(), name='equipment-list'),
    path('equipment/detail/<int:pk>/', equipment.EquipmentRetrieveAPIView.as_view(), name='equipment-detail'),
    path('equipment/update/<int:pk>/', equipment.EquipmentUpdateAPIView.as_view(), name='equipment-update'),
    path('equipment/delete/<int:pk>/', equipment.EquipmentDestroyAPIView.as_view(), name='equipment-delete'),

    # equipment_name
    path('equipment-name/list/', equipment_name.EquipmentNameListAPIView.as_view(), name='equipment-name-list'),

    # equipment_category
    path('equipment-category/list/', equipment_category.EquipmentCategoryListAPIView.as_view(),
         name='equipment-category-list'),
]
