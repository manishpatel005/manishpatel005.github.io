from collections import defaultdict
from math import sqrt
# Round off till 2 decimal places
NUM_DECIMAL = 2

outlink_list = defaultdict(list)
outlink_list['attention'] = ['attention', 'nmt']
outlink_list['bert'] = ['attention', 'bert', 'nmt']
outlink_list['nmt'] = []

inlink_list = defaultdict(list)
inlink_list['attention'] = ['attention', 'bert']
inlink_list['bert'] = ['bert']
inlink_list['nmt'] = ['attention', 'bert']

hub = {}
auth = {}
for k, _ in outlink_list.items():
    hub[k] = 1
    auth[k] = 1

print("round number 0:")
print(hub)
print(auth)
print('\n')

for i in range(10):
    print("round number:", i+1)
    # Calulcate new hub score
    new_hub = defaultdict(int)
    norm = 0
    for key,val in outlink_list.items():
        for v in val:
            new_hub[key] += auth[v]
        norm += (new_hub[key] * new_hub[key])
    norm = sqrt(norm)
    for k,v in new_hub.items():
        new_hub[k] = round(v / norm, NUM_DECIMAL)

    print('hub=',new_hub,' norm=',norm)
    # Calulcate new auth score
    new_auth = defaultdict(int)
    norm = 0
    for key,val in inlink_list.items():
        for v in val:
            new_auth[key] += hub[v]
        norm += (new_auth[key] * new_auth[key])
    norm = sqrt(norm)
    for k,v in new_auth.items():
        new_auth[k] = round(v / norm, NUM_DECIMAL)
    print('auth=', new_auth, ' norm=', norm)
    print('\n')
    hub = new_hub
    auth = new_auth
