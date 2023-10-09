# Import necessary modules
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# Define URL patterns
urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),

    # URLs for user authentication using allauth
    path('accounts/', include('allauth.urls')),

    # Include URLs from the 'core' app with a 'core' namespace
    path('', include('core.urls', namespace='core'))
]

# Include debug_toolbar URLs if DEBUG mode is enabled
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

    # Serve media files during development
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    # Serve static files during development
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
