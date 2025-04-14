from django.urls import include, path
from rest_framework.routers import DefaultRouter
from VehicleApi import views

router = DefaultRouter()
router.register('add', views.addVehicleView)

urlpatterns = [
    path('', include(router.urls)),
    path('vehicle/<int:id>/', views.get_vehicle_by_id, name='get_vehicle_by_id')
]
