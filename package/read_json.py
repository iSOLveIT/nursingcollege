import json
from os.path import join, dirname, realpath
from datetime import datetime as dt


directory = join(dirname(realpath(__file__)), 'data')
courseJson_path = directory + '/course.json'
questionJson_path = directory + '/question.json'
examdetailJson_path = directory + '/examdetail.json'
examremarksJson_path = directory + '/examremarks.json'


def course_db():
    """This function reads data from a json file
        
        Returns:
            content {[dict}] - A python object that contains the json data from the file
        """
    
    with open(courseJson_path, 'r') as f:
        content = json.load(f)
    return content


def question_db():
    """This function reads data from a json file
        
        Returns:
            content {[dict}] - A python object that contains the json data from the file
        """
    
    with open(questionJson_path, 'r') as f:
        content = json.load(f)
    return content


def examdetail_db():
    """This function reads data from a json file
        
        Returns:
            content {[dict}] - A python object that contains the json data from the file
    """
    
    with open(examdetailJson_path, 'r') as f:
        content = json.load(f)
    return content


class ExamRemarks:
    
    @staticmethod
    def showremarks():
        """This function reads data from a json file
        
        Returns:
            content {[dict}] - A python object that contains the json data from the file
        """
        
        with open(examremarksJson_path, 'r') as f:
            content = json.load(f)
        return content

    @staticmethod
    def updateremarks(course_code, exam_code, user_id, content):
        """This function write data into a json file
        
        Arguments:
            course_code {[str]} - The code of a course
            exam_code {[str]} - The code of an exam
            user_id {[int]} - The id of a student
            content {[str]} - A statement containing the marks a student had
        Returns:
            None
        """
        
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
                            else:
                                continue

        with open(examremarksJson_path, 'w') as f:
            json.dump(data, f, indent=4, sort_keys=True)
