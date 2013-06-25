#from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *
from OSPUPython.functions import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'^$', hello),
    (r'^time/plus(\d{1,2})/$', hours),
    (r'^timer/$', timer),
    (r'^square/$', square_print),
    (r'^square_print/$', square),

    (r'^triangle/$', triangle_print),
    (r'^triangle_print/$', triangle),
    (r'^circle/$', circle_print),
    (r'^circle_print/$', circle),
    (r'^paral/$', paral_print),
    (r'^paral_print/$', paral),
    (r'^demo/$', demo),


)
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
