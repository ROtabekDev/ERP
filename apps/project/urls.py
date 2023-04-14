from django.urls import path

from .api_endpoints import project, client, project_category, organization

urlpatterns = [
    # project
    path('create/', project.ProjectCreateAPIView.as_view(), name='project-create'),
    path('list/', project.ProjectListAPIView.as_view(), name='project-list'),
    path('detail/<int:pk>/', project.ProjectRetrieveAPIView.as_view(), name='project-detail'),
    path('update/<int:pk>/', project.ProjectUpdateAPIView.as_view(), name='project-update'),
    path('delete/<int:pk>/', project.ProjectDestroyAPIView.as_view(), name='project-delete'),

    # client
    path('client/create/', client.ClientCreateAPIView.as_view(), name='client-create'),
    path('client/list/', client.ClientListAPIView.as_view(), name='client-list'),
    path('client/update/<int:pk>/', client.ClientUpdateAPIView.as_view(), name='client-update'),
    path('client/delete/<int:pk>/', client.ClientDestroyAPIView.as_view(), name='client-delete'),

    # organization
    path('organization/create/', organization.OrganizationCreateAPIView.as_view(), name='organization-create'),
    path('organization/list/', organization.OrganizationListAPIView.as_view(), name='organization-list'),
    path('organization/update/<int:pk>/', organization.OrganizationUpdateAPIView.as_view(), name='organization-update'),
    path('organization/delete/<int:pk>/', organization.OrganizationDestroyAPIView.as_view(), name='organization-delete'),

    # project_category
    path('project-category/create/', project_category.ProjectCategoryCreateAPIView.as_view(), name='project-category-create'),
    path('project-category/list/', project_category.ProjectCategoryListAPIView.as_view(), name='project-category-list'),
    path('project-category/update/<int:pk>/', project_category.ProjectCategoryUpdateAPIView.as_view(), name='project-category-update'),
    path('project-category/delete/<int:pk>/', project_category.ProjectCategoryDestroyAPIView.as_view(), name='project-category-delete'),
]