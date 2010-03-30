from django.conf.urls.defaults import *
from twitter.profiles import views
from twitter.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^user_page/(.+)$', views.UserPage),
	(r'^home_page/$', HomePage),
	(r'^following/(.+)$', views.UserFollowing),
	(r'^followers/(.+)$', views.UserFollowers),
	(r'^login/$',LogIn),
	(r'^logout/$',LogOut),


    # Example:
    # (r'^twitter/', include('twitter.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
)
