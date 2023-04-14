from django.urls import path

from .api_endpoints import employee, position, address

urlpatterns = [
    # employee
    path('create/', employee.EmployeeCreateAPIView.as_view(), name='employee-create'),
    path('list/', employee.EmployeeListAPIView.as_view(), name='employee-list'),
    path('detail/<int:pk>/', employee.EmployeeRetrieveAPIView.as_view(), name='employee-detail'),
    path('update/<int:pk>/', employee.EmployeeUpdateAPIView.as_view(), name='employee-update'),
    path('delete/<int:pk>/', employee.EmployeeDestroyAPIView.as_view(), name='employee-delete'),

    # position
    path('position/list/', position.PositionListAPIView.as_view(), name='position-list'),

    # address
    path('address/list/', address.AddressListAPIView.as_view(), name='address-list'),
    path('region/list/', address.RegionListAPIView.as_view(), name='region-list'),
    path('district/list/', address.DistrictListAPIView.as_view(), name='district-list'),

]