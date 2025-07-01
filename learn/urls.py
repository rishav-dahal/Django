
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('template_example.urls')),
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('employees/', include('employees.urls')),
    path('blogs/',include('blogs.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
