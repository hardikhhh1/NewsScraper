import celery
from hackernews import HackerNews
from models import StoryModel
from bs4 import BeautifulSoup
import urllib2


@celery.task
def scrape_hacker_news():
	hn = HackerNews()
	item_id_list = hn.top_stories()
	stories_list = []
	for item_id in item_id_list:
		print item_id
		try:
			# is_pres_count = StoryModel.objects.filter(story_id=item_id).count()

			# if (is_pres_count > 0):
			# 	continue
		
			try:
				hn_story = hn.get_item(item_id)
				# print hn_story
				page = urllib2.urlopen(hn_story.url)
				bs = BeautifulSoup(page.read())

				content = bs.get_text()
				content = ' '.join(word for word in content.split('\n') if word != '')
				story = StoryModel(story_id =hn_story.item_id,
					title=hn_story.title,
					link=hn_story.url,
					points=hn_story.score,
					# content = content,
					# submitter=hn_story
					published_time=hn_story.submission_time)
				# story.save()
				
				stories_list.append(story)
			except Exception as e:
				print("error while retrieving : %s" % (e))
				continue
		except Exception as e:
				print("error while retrieving : %s" % (e))
				continue
	print("the size of the story list is %s" %(len(stories_list)))
	return stories_list
			# story.save()
		


