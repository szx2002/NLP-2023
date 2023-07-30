from gensim.test.utils import common_texts
import gensim.downloader as api
from sklearn.metrics.pairwise import cosine_similarity

import gensim.downloader
print(list(gensim.downloader.info()['models'].keys()))

import gensim.downloader as api
#wv = api.load('word2vec-google-news-300')
model = api.load("glove-twitter-25")

model.most_similar("glass")

v_apple = model['banana']
v_mango = model['mango']
cosine_similarity([v_apple],[v_mango])

model.most_similar('computer', topn=10)

pairs = [
    ('car', 'vehicle'),   # a minivan is a kind of car
    ('car', 'bicycle'),   # still a wheeled vehicle
    ('car', 'airplane'),  # ok, no wheels, but still a vehicle
    ('car', 'cereal'),    # ... and so on
    ('car', 'communism'),
]
for w1, w2 in pairs:
    print('%r\t%r\t%.2f' % (w1, w2, model.similarity(w1, w2)))
    
    
model.most_similar(positive=['uk', 'paris'], negative=['france'], topn=5)
model.most_similar(positive=['england', 'paris'], negative=['france'], topn=5)
[('liverpool', 0.867056131362915),
 ('city', 0.8668259382247925),
 ('london', 0.8529374599456787),
 ('captain', 0.8526314496994019),
 ('stadium', 0.8468754291534424)]


