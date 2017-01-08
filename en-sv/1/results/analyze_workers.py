from collections import defaultdict

worker_to_topic = defaultdict(list)

for line in open('f980709.csv'):

    if '_unit_id' in line: continue

    linebreak   =   line.strip().split(',')
    worker_id   =   int(linebreak[9])
    key_topic   =   int(linebreak[21])
    cand1       =   int(linebreak[15])
    cand2       =   int(linebreak[16])
    cand3       =   int(linebreak[17])

    worker_to_topic[worker_id].append(key_topic)
    worker_to_topic[worker_id].append(cand1)
    worker_to_topic[worker_id].append(cand2)
    worker_to_topic[worker_id].append(cand3)

a = []

for worker_id in worker_to_topic:
    total_keys  =   len(worker_to_topic[worker_id])
    repeated    =   total_keys-len(set(worker_to_topic[worker_id]))
    print(worker_id, repeated/total_keys)
    a.append(repeated/total_keys)


import numpy as np 

print(np.mean(a))