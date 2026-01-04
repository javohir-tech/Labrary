from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Books Api",
        default_version="v1",
        description="Labrary demo project",
        terms_of_service="demo.com",
        contact=openapi.Contact(email="suvonovjavohir625@gmail.com"),
        license=openapi.License(name="MIT Licence"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("books.urls")),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/registration/", include("dj_rest_auth.registration.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swaggre-ui",
    ),
    path(
        "redoc/", schema_view.with_ui("redoc", cache_timeout=9), name="schema-redoc-ui"
    ),
]
