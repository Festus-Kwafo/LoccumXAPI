from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.schemas import get_schema_view 

schema_view = get_schema_view(title='LoccumX API') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/login/', include('rest_auth.registration.urls')),
    path('api/v1/', include('accounts.urls', namespace='api')),
    path('api/v1/', include('loccumApi.urls', namespace='loccumApi')),
    path('schema/', schema_view),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
