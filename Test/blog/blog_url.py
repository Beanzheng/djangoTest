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

    url(r'/v10_1',views.v10_1),
    url(r'/v10_2',views.v10_2),
    url(r'/v11_hello',views.v11, name="hello"),
    url(r'/getRsq/',views.getReqContent),
    url(r'/blog_get',views.blog_get),
    url(r'/blog_post',views.blog_post),
    url(r'/render_test',views.render_test),
    url(r'render2_test',views.render2_test),
    url(r'render3_test',views.render3_test),
    url('/get404',views.get404),
]
