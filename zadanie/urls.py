from django.conf.urls import patterns, include, url

from django.contrib import admin
# admin.autodiscover()
from users.views import UsersView, UsersDelete, UsersUpdate, UsersCreate

urlpatterns = patterns('',
    # Examples:
    url(r'^$', UsersView.as_view()),
    url(r'^add/$', UsersCreate.as_view(), name='user_add'),
    url(r'^(?P<pk>[0-9]+)/$', UsersUpdate.as_view(), name='user_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', UsersDelete.as_view(), name='user_delete'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
