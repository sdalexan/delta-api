from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'data', views.DataListViewSet)
router.register(r'alert', views.AlertListViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'policy', views.PolicyViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]