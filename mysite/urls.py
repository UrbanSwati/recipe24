from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^recipes/', include('recipes.urls'), name="recipes"),
    url(r'^about/$',views.aboutpage, name="about"),
    url(r'^$', views.homepage, name="home"),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)