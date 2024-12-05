from n9admin.views import create_welcome, get_welcome, serve_media, create_idea, get_ideas, create_client, get_clients, create_archive, get_archives
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="N9 Agencia API",
        default_version='v1',
        description="Descrição da API",
        terms_of_service="https://n9agency.site/terms/",
        contact=openapi.Contact(email="suporte@n9agency.site"),
        license=openapi.License(name="n9agency.site.license"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome', create_welcome, name="welcome"), #Configurações de Boas vindas
    path('config', get_welcome), #Lista configurações de boas vindas
    path('media/<path:path>/', serve_media), #lista imagem
    path('idea', create_idea), #cria ideia
    path('ideas', get_ideas), #lista ideias
    path('portfolio', create_client), #cria portfolio
    path('clients', get_clients), #lista clientes
    path('send', create_archive), #envia arquivos de cliente
    path('archives', get_archives),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
