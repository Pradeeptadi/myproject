'''from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from blog import views

urlpatterns = [
    path('', views.home, name='home'),  # root URL points to home view
    path('page/', views.page),          # optional, if you want this
    path('blog/', include('blog.urls')), # if you have separate blog urls
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
'''from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from blog import views

urlpatterns = [
    path('', views.home, name='home'),  # root URL points to home view
    path('page/', views.page),          # optional, if you want this
    path('blog/', include('blog.urls')), # if you have separate blog urls
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
from django.contrib import admin
from django.urls import path, include
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
  ##  path('post/', include('blog.urls')),  # Make sure this is included
    path('', views.home, name='home'),
    path('page/', views.page),          # optional, if you want this
    path('blog/', include('blog.urls')), # if you have separate blog urls
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)