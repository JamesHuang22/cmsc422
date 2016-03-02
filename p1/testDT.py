from numpy import *
from pylab import *
import util, datasets, runClassifier, binary, dt

h = dt.DT({'maxDepth': 1})
print(h)

# print(h.predict(h, X=2))
h.train(datasets.TennisData.X, datasets.TennisData.Y)
print(h)

h = dt.DT({'maxDepth': 2})
h.train(datasets.TennisData.X, datasets.TennisData.Y)
print(h)

h = dt.DT({'maxDepth': 5})
h.train(datasets.TennisData.X, datasets.TennisData.Y)
print(h)

# Sentiment data
h = dt.DT({'maxDepth': 2})
h.train(datasets.SentimentData.X, datasets.SentimentData.Y)
print(h)

print(datasets.SentimentData.words[2428])
print(datasets.SentimentData.words[3842])
print(datasets.SentimentData.words[3892])

runClassifier.trainTestSet(dt.DT({'maxDepth': 1}), datasets.SentimentData)