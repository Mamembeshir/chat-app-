from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from server.views import ServerListViewSet
router=DefaultRouter()
router.register("api/server/select",ServerListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls
