from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.documentation import include_docs_urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('product_api.urls')),
    path('docs/', include_docs_urls(title='Product API')), # Api Documentation endpoint    
]
