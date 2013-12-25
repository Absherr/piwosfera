from django.conf.urls import patterns, include, url
import os
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'piwosfera.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^$','main.views.home_view'),
    (r'^site_media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), 'site_media')}),
    url(r'^admin/', include(admin.site.urls)),
)
