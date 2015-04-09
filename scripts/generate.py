import json
import random
import sys

random.seed(int(sys.argv[1]))
N = int(sys.argv[2])
with open('data/sample_a.json', 'w') as f_sample_a, open('data/sample_b.json', 'w') as f_sample_b:
    for i in xrange(N):
        r = random.random()
        if r >= 0.1:
            f_sample_a.write(json.dumps(dict(
                key=str(i),
                foo=i
            )))
            f_sample_a.write('\n')

        if r < 0.9:
            f_sample_b.write(json.dumps(dict(
                key=str(i),
                bar=i * N,
                other='foobar',
                this='that',
                that='this',
                some='thing',
            )))
            f_sample_b.write('\n')
