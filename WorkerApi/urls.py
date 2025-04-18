#Import the necessary modules
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from WorkerApi import views

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register('add', views.addWorkerView)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('worker/<int:id>/', views.get_worker_by_id, name='get_worker_by_id')
]