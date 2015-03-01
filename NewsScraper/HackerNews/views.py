from django.shortcuts import render
from rest_framework import generics, permissions
from serializers import StorySerializers
from models import StoryModel
from rest_framework import viewsets
# from django import csrf_protect, ensure_csrf_cookie




# @csrf_protect
# @ensure_csrf_cookie
def index(request):
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