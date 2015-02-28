from django.test import TestCase
# from HackerNews import scraper
from HackerNews.models import StoryModel
from hackernews import HackerNews

import scraper, datetime

class HackerNewsTest(TestCase):

	# def test_save_item(self):
	
	def test_save_item(self):

		story_model = StoryModel(title=item.title, 
				text       	   = item.text,
				link    	   = item.url,
				# domain  	   = item.domain,
				points    	   = item.score,
				submitter      = item.by,
				published_time = item.submission_time,
				# num_comments   = item.num_comments
				)
		story_model.save()
		print("saved to the database")
		# hn = HackerNews()

		# top_story_ids = hn.top_stories()
		# print(top_story_ids)
		# print(top_story_ids[:1])
		# for story_id in top_story_ids[:1]:
			# print(story_id)
			# item = hn.get_item(story_id)
			# if(item.item_type  == 'story'):
				# print(item.submission_time)


			# story_model = StoryModel(title=item.title, 
			# 	text       	   = item.text,
			# 	link    	   = item.url,
			# 	# domain  	   = item.domain,
			# 	points    	   = item.score,
			# 	submitter      = item.by,
			# 	published_time = item.submission_time,
			# 	# num_comments   = item.num_comments
			# 	)
			# story_model.save()
			# print("saved to the database")



	
