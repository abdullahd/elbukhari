from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# Try to import from newer Wagtail versions first
try:
    from wagtail import urls as wagtail_urls
    from wagtail.admin import urls as wagtailadmin_urls
    from wagtail.documents import urls as wagtaildocs_urls
except ImportError:
    # Fall back to older import paths
    from wagtail.core import urls as wagtail_urls
    from wagtail.admin import urls as wagtailadmin_urls
    from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    # Django Admin
    path('django-admin/', admin.site.urls),
    
    # Wagtail Admin
    path('admin/', include(wagtailadmin_urls)),
    
    # Wagtail Documents
    path('documents/', include(wagtaildocs_urls)),
    
    # Your app URLs
    path('', include('app.urls')),
    
    # Wagtail URLs - these should be last as they're the most general
    path('', include(wagtail_urls)),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 