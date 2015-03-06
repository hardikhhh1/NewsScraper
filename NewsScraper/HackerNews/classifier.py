from HackerNews.models import StoryModel
from nltk.stem.snowball import EnglishStemmer
from sklearn.feature_extraction import text
from sklearn import preprocessing
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from nltk.corpus import stopwords
import numpy as np
from scraper import scrape_hacker_news

def temp_method():
	categories = ['good' , 'bad']

	print("test111")
	stories = StoryModel.objects.all()
	
	stemmer = EnglishStemmer()
	# stop_words = stopwords.words('english')
	x_train = np.array([])
	y_train = np.array([])
	target_names = np.array(['good', 'bad'])
	for story in stories:
		story_data = story.content
		# stemmed_story_data = ' '.join(stemmer.stem(word) for word in story_data.split(' '))
		# stemmed_story_data = ' '.join(stemmer.stem(word for word in story_data.split(' ')))
		# stoped_story_data = ' '.join(word for word in stemmed_story_data.split() if word not in stop_words)
		x_train = np.append(x_train,[story_data])
		 
		
		# print(x_train)
		if story.is_interested == False:
			y_train = np.append(y_train,[0])
		else:
			y_train = np.append(y_train,[1])

		# lb = preprocessing.LabelBinarizer()
		# Y = x_.fit_transform(y_train)

		classifier = Pipeline([('vectorizer', CountVectorizer(ngram_range=(1, 2))),
	    ('tfidf', TfidfTransformer()),
	    ('clf', MultinomialNB())])

	classifier.fit(x_train, y_train)

	# for label  in np.nditer(y_train):
	# 	print label
	new_stories_list = scrape_hacker_news()
	x_test = np.array([])
	for story in new_stories_list:
		story_data = story.content
		# print("2222")
		# stemmed_story_data = ' '.join(stemmer.stem(word) for word in story_data.split(' '))
		# print("33333")
		# stoped_story_data = ' '.join(word for word in stemmed_story_data.split() if word not in stop_words)
		# print("44444")

		# (' '.join(stemmer.stem(x) for x in input.split()))


		x_test = np.append(x_test, [story_data])

	predicted = classifier.predict(x_test)
	# all_labels = lb.inverse_transform(predicted)

	index = 0
	for label  in np.nditer(predicted):
		print("label : %s , index : %s" %(label, index))
		story = new_stories_list[index]
		if label == 1:
			story.is_interested = True
			# story.save()

		else:
			story.is_interested = False
		index += 1
		print story.title + " : " + label
			# story.save()







