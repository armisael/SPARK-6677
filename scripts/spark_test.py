"""
These lines, when copy-pasted in pyspark, sometimes raise an exception:
  File "<stdin>", line 4, in <module>
  File ".../spark-1.3.0-bin-hadoop2.4/python/pyspark/sql/types.py", line 1214, in __repr__
    for n in self.__FIELDS__))
  File ".../spark-1.3.0-bin-hadoop2.4/python/pyspark/sql/types.py", line 1214, in <genexpr>
    for n in self.__FIELDS__))
IndexError: tuple index out of range

The same does not apply using spark-submit
"""
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext

conf = SparkConf()
sc = SparkContext("local", "Simple App", conf=conf)
sqlCtx = SQLContext(sc)

from operator import attrgetter
x = sqlCtx.jsonFile("data/sample_a.json").rdd.keyBy(attrgetter('key'))
y = sqlCtx.jsonFile("data/sample_b.json").rdd.keyBy(attrgetter('key'))
for result in x.cogroup(y).collect():
    key, (res_x, res_y) = result
    print "key:", key
    print "res1 data as row:", list(res_x)
    print "res2 data as row:", list(res_y)
    if res_x.maxindex > 0 and res_y.maxindex > 0:
        print "res1 and res2 fields:", res_x.data[0].__FIELDS__, res_y.data[0].__FIELDS__
        print "res1 data as tuple:", res_x.data[0][0], res_x.data[0][1]
        print "res2 data as tuple:", res_y.data[0][0], res_y.data[0][1], res_y.data[0][2]
