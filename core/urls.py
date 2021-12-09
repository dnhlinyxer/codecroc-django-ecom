"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop.admin import shop_admin

from shop.views import home, test2, http_response, redirect_view, post_view, product_detail_view

urlpatterns = [
    path('', home),
    path('shop/', include('shop.urls', namespace='shop')),
    path('auth/', include('django.contrib.auth.urls')),
    path('test2/', test2),
    path('http_response/', http_response),
    path('post/', post_view),
    #path('product-detail/', product_detail_view),
    path('redirect/', redirect_view),
    path('admin/', admin.site.urls),
    path('shop_admin/', shop_admin.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

admin.site.index_title = 'Django Ecom 後台'
admin.site.site_header = 'CodeCroc 管理'
admin.site.site_title = 'CodeCroc Ecom'
