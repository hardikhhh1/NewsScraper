from django.test import TestCase
# from HackerNews import scraper
from HackerNews.models import StoryModel
from hackernews import HackerNews

import scraper, datetime

class HackerNewsTest(TestCase):

	# def test_save_item(self):
	
	def test_save_item(self):

		hn = HackerNews()
		item_id_list = hn.top_stories()
		for item_id in item_id_list[:5]:
			
			try:
				is_pres_count = StoryModel.objects.filter(story_id=item_id).count()

				if (is_pres_count == 0):
					continue
			except Exception as e:
				print("Error occured : %s" % (e))
				continue

			hn_story = hn.get_item(item_id)
			story = StoryModel(title=hn_story.title,
				link=hn_story.url,
				points=hn_story.score,
				# submitter=hn_story
				published_time=hn_story.submission_time)
			story.save()