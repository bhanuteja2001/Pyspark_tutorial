from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)
print("Hello")
lines = sc.textFile("file:///Tutorial/ml-100k/u.data")
print(lines)
ratings = lines.map(lambda x: x.split()[2])
print(ratings)
result = ratings.countByValue()

sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print("%s %i" % (key, value))
