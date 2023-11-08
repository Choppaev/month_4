from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),
    path('', include('tvshow.urls')),
    path('', include('parser_app.urls')),
    path('', include('custom_user.urls')),
    path('', include('cloth.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
