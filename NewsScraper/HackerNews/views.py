from django.shortcuts import render
from rest_framework import generics, permissions
from serializers import StorySerializers
from models import StoryModel
from rest_framework import viewsets
from HackerNews import classifier
# from django import csrf_protect, ensure_csrf_cookie




# @csrf_protect
# @ensure_csrf_cookie
def index(request):

    from HackerNews.scraper import scrape_hacker_news
    try:
        # stories_list = scrape_hacker_news()
        # classifier.temp_method()
        pass
        # StoryModel.objects.bulk_create(stories_list)
    except Exception as e:
        print('not able to get the list')

    return render(request, 'index.html')



class StoryListView(generics.ListCreateAPIView):
    queryset = StoryModel.objects.all()
    serializer_class = StorySerializers


class StoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StoryModel.objects.all()
    serializer_class = StorySerializers
    permission_classes = [
        permissions.AllowAny
    ]


class HomePageView(viewsets.ModelViewSet):
	queryset = StoryModel.objects.all()
	serializer_class = StorySerializers



# class TweetViewSet(viewsets.ModelViewSet):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsAuthorOrReadOnly,)

#     def pre_save(self, obj):
#         obj.user = self.request.user