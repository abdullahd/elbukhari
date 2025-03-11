from django.urls import path, include
from django.contrib import admin
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls

urlpatterns = [
    # ... other patterns ...
    path('admin/', admin.site.urls),
    path('cms/', include(wagtailadmin_urls)),
    
    # Include the app URLs with namespace explicitly
    path('', include(('app.urls', 'app'), namespace='app')),
    
    # Wagtail's catch-all URL pattern should be last
    path('', include(wagtail_urls)),
] 