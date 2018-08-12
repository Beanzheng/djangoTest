'''
住url
'''
from django.conf.urls import include, url
from django.contrib import admin
from blog import blog_url
urlpatterns = [
    # Examples:
    # url(r'^$', 'Test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^Blog',include(blog_url))
]
