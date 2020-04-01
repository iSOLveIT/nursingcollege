import json
from os.path import join, dirname, realpath
from datetime import datetime as dt


directory = join(dirname(realpath(__file__)), 'data')
courseJson_path = directory + '/course.json'
questionJson_path = directory + '/question.json'
examdetailJson_path = directory + '/examdetail.json'
examremarksJson_path = directory + '/examremarks.json'


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


class ExamRemarks:
    """This class contains methods for showing and updating participants data for exam
    """
    @staticmethod
    def showremarks():
        with open(examremarksJson_path, 'r') as f:
            content = json.load(f)
        return content

    @staticmethod
    def updateremarks(course_code, exam_code, user_id, content):
        data = ExamRemarks.showremarks()

        for item in data:
            if item['courseCode'] == course_code:
                for exam in item['exams']:
                    if exam['examCode'] == exam_code:
                        for user in exam['participants']:
                            if user['userID'] == user_id:
                                user['submissionStatus'] += 1
                                user['gradingStatus'] = content
                                user['dateModified'] = dt.now().strftime("%d-%m-%Y, %I:%M %p")

        with open(examremarksJson_path, 'w') as f:
            json.dump(data, f, indent=4, sort_keys=True)

    

"""
#data = course_db()
#with open(json_path, 'w') as file:
    #for item in data:
     #   item.update(username="Tetteh Lord")
    #json.dump(data, file, indent=2, sort_keys=True)
#print(len(data[0]))
#print(examdetail_db())
"""
