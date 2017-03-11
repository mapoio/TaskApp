from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
import company.views as views


route = DefaultRouter()
route.register(r'company',views.CompanyViewSet)
route.register(r'department',views.DepartmentViewSet)

urlpatterns = [
    url(r'^',include(route.urls))
]
