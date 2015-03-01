from django.conf.urls import patterns, include, url
from django.contrib import admin
from HackerNews.views import StoryListView, StoryDetailView, index
from rest_framework.routers import DefaultRouter
from django.contrib import admin




urlpatterns = patterns('',
    # Examples:
    
    
    url(r'^api/story/$', StoryListView.as_view()),
    url(r'^api/story/(?P<pk>[0-9]+)/$', StoryDetailView.as_view()),
    url(r'^$', index, name='index')
)




# admin.autodiscover()

# router = DefaultRouter()
# router.register(r'tweets', views.TweetViewSet)
# router.register(r'users', views.UserViewSet)

# urlpatterns = patterns('',
#                        url(r'^admin/', include(admin.site.urls)),
#                        url(r'^api/', include(router.urls)),
#                        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#                        url(r'^$', views.index, name='index'),
# )

