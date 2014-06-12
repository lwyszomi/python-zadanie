from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()
from users.views import UsersView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', UsersView.as_view()),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
