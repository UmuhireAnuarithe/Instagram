from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^search/', views.search_user, name='search_user'),
    url(r'^new/profile$', views.new_profile, name='new-profile'),
    url(r'^profile/$',views.profile,name = 'profile'),
    url(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)