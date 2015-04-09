# SPARK-6677

This repository contains a docker to reproduce [SPARK-6677](https://issues.apache.org/jira/browse/SPARK-6677); to run it, just clone and:
```
docker build -t spark6677 .
docker run -i -t spark6677
```

This should fail with:
```python
key: 11547
res1 data as row: [Row(foo=11547, key=u'11547')]
res2 data as row: [Row(foo=577350000, key=u'11547')]
res1 and res2 fields: (u'foo', u'key') (u'foo', u'key')
res1 data as tuple: 11547 11547
res2 data as tuple: 577350000 11547 foobar
key: 38843
res1 data as row: [Traceback (most recent call last):
  File "/home/ubuntu/spark/scripts/spark_test.py", line 25, in <module>
    print "res1 data as row:", list(res_x)
  File "/home/ubuntu/spark/python/pyspark/sql/types.py", line 1214, in __repr__
    for n in self.__FIELDS__))
  File "/home/ubuntu/spark/python/pyspark/sql/types.py", line 1214, in <genexpr>
    for n in self.__FIELDS__))
IndexError: tuple index out of range
```

Tested with docker 1.5.0 (build a8a31ef) and 1.2.0 (build fa7b24f)
