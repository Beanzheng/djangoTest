'''
子url
'''

from django.conf.urls import include, url
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'Test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'do_normal',views.do_normal),
    url(r'withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])',views.withparam),
    url(r'book/(?:page-(?P<pagenumber>\d+)/)?$',views.findNumber),
    url(r'yourname',views.extraparam,{"name":"郑高翔"}),
    url(r'mayiknowyouname/$',views.revParse,name="askname"),
]
