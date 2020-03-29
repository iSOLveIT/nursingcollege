import json
from os.path import join, dirname, realpath


directory = join(dirname(realpath(__file__)), 'data')
courseJson_path = directory + '/course.json'
questionJson_path = directory + '/question.json'
examdetailJson_path = directory + '/examdetail.json'

def course_db():
    with open(courseJson_path, 'r') as f:
        content = json.load(f)
    return content


def question_db():
    with open(questionJson_path, 'r') as f:
        content = json.load(f)
    return content


def examdetail_db():
    with open(examdetailJson_path, 'r') as f:
        content = json.load(f)
    return content

#data = course_db()
#with open(json_path, 'w') as file:
    #for item in data:
     #   item.update(username="Tetteh Lord")
    #json.dump(data, file, indent=2, sort_keys=True)
#print(len(data[0]))
#print(examdetail_db())