import json
import pandas as pd
from pprint import pprint
with open('source_file_2.json') as json_data:
    data = json.load(json_data)
#pprint(data)

# Sorting it by ascending order based on priority, lower priority number means higher priority.
lists =  (sorted(data, key = lambda i:i['priority']))
pprint(lists)
manager = []
watcher = []
for items in lists:
    manager.append(items['managers'])
    watcher.append(items['watchers'])
    
# Taking out the list of managers and watchers
import itertools
merged_manager = list(itertools.chain.from_iterable(manager))
merged_watcher = list(itertools.chain.from_iterable(watcher))

# converting them to a dictionary removes all duplicates, converting them back to lists
merged_manager = list(dict.fromkeys(merged_manager))
merged_watcher = list(dict.fromkeys(merged_watcher))

# Appending names to dictionary and adding
manager_json = dict()
for i in merged_manager:    
    for items in lists:
        if(i in items['managers']):
            manager_json.setdefault(i,[]).append(items['name'])
print(manager_json)

watcher_json = dict()
for i in merged_watcher:
    for items in lists:
        if(i in items['watchers']):
            watcher_json.setdefault(i, []).append(items['name'])
print(watcher_json)

# Writing into JSON files as requested
json_object_1 = json.dumps(manager_json, indent=4)
json_object_2 = json.dumps(watcher_json, indent=4)
with open("managers.json", "w") as outfile:
    outfile.write(json_object_1)
with open("watchers.json", "w") as outfile:
    outfile.write(json_object_2)


