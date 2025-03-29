import json

sample_array = {"1": "line 1", "2": "line 2", "3": "line 3", "4": "line 4", "5": "line 5", "6": "line 6", "7": "line 7"}
json_str = json.dumps(sample_array, indent=7)
print(json_str)
file_descriptor = open(r'lesson5.json', 'w')
file_descriptor.write(json_str)
file_descriptor.close()
file_descriptor = open('lesson5.json', 'r')
json_str = file_descriptor.read()
sample_array2 = json.loads(json_str)
print(sample_array2)
print(sample_array)

