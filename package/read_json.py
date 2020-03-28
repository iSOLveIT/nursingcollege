import json
from os.path import join, dirname, realpath


directory = join(dirname(realpath(__file__)), 'data')
json_path = directory + '/course.json'

def course_db():
    with open(json_path, 'r') as f:
        content = json.load(f)
    return content

#data = course_db()
#with open(json_path, 'w') as file:
    #for item in data:
     #   item.update(username="Tetteh Lord")
    #json.dump(data, file, indent=2, sort_keys=True)
#print(len(data[0]))