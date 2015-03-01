

from rest_framework import serializers
from models import StoryModel



class StorySerializers(serializers.ModelSerializer):
	class Meta:
		model = StoryModel
		fields = ( 'id','story_id', 'title', 'link', 'points',
			'submitter','published_time', 'is_interested', 'content')


