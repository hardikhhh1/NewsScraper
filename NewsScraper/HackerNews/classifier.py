from HackerNews.models import StoryModel
from nltk.stem.snowball import EnglishStemmer
from sklearn.feature_extraction import text
from sklearn import preprocessing
from sklearn.pipeline import Pipeline
from nltk.corpus import stopwords
import numpy as np
from scraper import scrape_hacker_news

def temp_method():
	categories = ['good' , 'bad']


	stories = StoryModel.object.all()

	stemmer = EnglishStemmer()
	stop_words = stopwords.words('english')
	x_train = np.array([])
	y_train = np.array([])
	target_names = np.array['good', 'bad']
	for story in stories:
		story_data = story.data
		stemmed_story_data = ' '.join(stemmer.stem(word for word in story_data.split(' ')))
		stoped_story_data = ' '.join(word for word in stemmed_story_data.split() if word not in stop_words)
		x_train.append(stoped_story_data)
		if story.is_interested == False:
			y_train.append('bad')
		else:
			y_train.append('good')

		lb = preprocessing.LabelBinarizer()
		Y = lb.fit_transform(y_train)

		classifier = Pipeline([('vectorizer', CountVectorizer()),
	    ('tfidf', TfidfTransformer()),
	    ('clf', OneVsRestClassifier(LinearSVC()))])

	classifier.fit(x_train, Y)

	new_stories_list = scrape_hacker_news()
	x_test = np.array([])
	for story in stories:
		story_data = story.data
		stemmed_story_data = ' '.join(stemmer.stem(word for word in story_data.split(' ')))
		stoped_story_data = ' '.join(word for word in stemmed_story_data.split() if word not in stop_words)
		x_test.append(stoped_story_data)

	predicted = classifier.predict(x_test)
	all_labels = lb.inverse_transform(predicted)

	for index, label in all_labels:
		story = new_stories_list[index]
		if label == "good":
			story.is_interested = True
			story.save()

		else:
			story.is_interested = False
			story.save()







