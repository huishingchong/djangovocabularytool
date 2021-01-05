from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mypages.urls')),
    path('', TemplateView.as_view(template_name="mypages/login.html")),
    path('accounts/', include('allauth.urls'))
]