"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from social_auth.views import GitHubLogin
from users.views import RegisterView, CustomTokenObtainPairView

schema_view = get_schema_view(
    openapi.Info(
        title="API - статьи игр",
        default_version="v1",
        description="API для управления статьями об играх",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games/', include('games.urls')),

    # Документация
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),

    # JWT-токены
    path('api/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    # Auth
    path('api/auth/register/', RegisterView.as_view()),
    path('api/auth/login/', CustomTokenObtainPairView.as_view()),
    path('api/auth/github/', GitHubLogin.as_view()),
    path('accounts/', include('allauth.urls')),
    path('accounts/github/login/callback/', GitHubLogin.as_view(), name='github_callback'),
]
