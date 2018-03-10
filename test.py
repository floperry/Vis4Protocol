from gensim.models import Word2Vec
from pprint import pprint
import re, string

class MyCorpus(object):
	def __init__(self, fname):
		self.fname = fname

	def __iter__(self):
		for line in open(self.fname):
			yield re.sub('[%s]' % re.escape(string.punctuation), '', line.lower().split())

sentences = MyCorpus('test.txt')

# sentences = [["cat", "say", "meow"], ["dog", "say", "woof"]]

model = Word2Vec(sentences, size=2, min_count=1)
say_vector = model['the']  # get vector for word
print(say_vector)

