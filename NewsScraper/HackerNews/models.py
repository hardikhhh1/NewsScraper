from django.db import models

# Create your models here.


class StoryModel(models.Model):
	story_id = models.IntegerField()
	title = models.CharField(max_length=100, default='')
	link = models.URLField(default='')
	# domain = models.CharField(max_length=200, default='')
	points = models.IntegerField(default=0000)
	submitter = models.CharField(max_length=100, default='')
	published_time = models.CharField(max_length=100, default='')
	is_interested = models.BooleanField(default=True)
	content = models.TextField(default="")
	# num_comments = models.IntegerField()

	def __str__(self):
		return "Title : %s , Points: %s , Time : %s" % (self.title , self.points, self.published_time)


	class Meta:
		verbose_name = "Story"
		verbose_name_plural = "Stories"

		

class StoryComments(models.Model):
	# comment_id = models.AutoField()
	comment_link = models.URLField(max_length=500)
	comment = models.CharField(max_length=1000, default='')
	story = models.ForeignKey(StoryModel)



