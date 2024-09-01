from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
"""
Defines the urlpatterns for the CocktailDB API endpoints including paths for retrieving cocktail data, accessing the Swagger UI, obtaining JWT tokens, and refreshing tokens.
"""
schema_view = get_schema_view(
   openapi.Info(
      title="CocktailDB API",
      default_version='v1',
      description="API for cocktail recipes and ingredients",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/', include('cocktails.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
