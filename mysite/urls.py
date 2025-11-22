from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('bookmark/', include('bookmark.urls')), 
    path('blog/', include('blog.urls')),
    path('photo/', include('photo.urls')),
]

if settings.DEBUG: # 개발 모드일 때만 작동
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)