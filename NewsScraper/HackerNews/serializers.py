

from rest_framework import serializers
from models import StoryModel



class StorySerializers(serializers.ModelSerializer):
	class Meta:
		model = StoryModel
		fields = ( 'id','story_id', 'title',  'is_interested')


# 'link', 'points',
# 			'submitter','published_time',