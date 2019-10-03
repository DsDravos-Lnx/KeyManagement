from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import AdminViewSet, KeyViewSet, UserViewSet, LendingViewSet

router = routers.DefaultRouter()
router.register(r'admins', AdminViewSet)
router.register(r'keys', KeyViewSet)
router.register(r'users', UserViewSet)
router.register(r'lendings', LendingViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
