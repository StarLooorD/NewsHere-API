from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/base-auth/", include("rest_framework.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("api/v1/news/", include("news.urls")),
]
