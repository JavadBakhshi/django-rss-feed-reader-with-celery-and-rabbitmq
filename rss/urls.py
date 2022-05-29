from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from . import views

router = routers.DefaultRouter()
router.register('', views.NewsView)

app_name = 'rss'
urlpatterns = [
    path('', views.home, name='home'),
    path('api/v1/', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),name='token_refresh'),
]
