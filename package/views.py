# Third-party modules
from flask.views import MethodView
from flask import render_template, request, redirect, url_for, flash, session

# Local modules
from package.read_json import course_db, question_db, examdetail_db
from package.helpers import ocr

# Built-in modules
import base64


class IndexEndpoint(MethodView):
    """View for Index Route
    
    Arguments:
        MethodView -- If you implement a request method (like GET), it will be used to handle GET requests.
    
    Returns:
        none
    """

    @staticmethod
    def get():
        """This function executes when request method for this route = get
        
        Returns:
            html template -- renders html template
        """
        return render_template('index.html', quiz=False), 200
    # This function executes when request method for this route = post

    # def post(self):
    # return redirect(url_for('index', _anchor='contact-section'))


class DashboardEndpoint(MethodView):
    """View for Dashboard Route
    
    Arguments:
        MethodView -- If you implement a request method (like GET), it will be used to handle GET requests.
    
    Returns:
        none
    """

    @staticmethod
    def get(user_id):
        """This function executes when request method for this route = get
        
        Returns:
            html template -- renders html template
        """
        data = course_db()
        content = []
        for item in data:
            if item['user'] == user_id:
                username = item['username']
                content.append(item)
                session['username'] = username
        session['course_details'] = content
        return render_template('dashboard.html', quiz=False), 200


class CoursesEndpoint(MethodView):
    """View for Course Route
    
    Arguments:
        MethodView -- If you implement a request method (like GET), it will be used to handle GET requests.
    
    Returns:
        none
    """

    @staticmethod
    def get(course_code):
        """This function executes when request method for this route = get
        
        Returns:
            html template -- renders html template
        """
        exam_detail = examdetail_db()
        return render_template('course.html',
                               course_code=course_code,
                               course_exam=exam_detail,
                               quiz=False), 200


class ExamdetailsEndpoint(MethodView):
    """View for Exam Details Route
    
    Arguments:
        MethodView -- If you implement a request method (like GET), it will be used to handle GET requests.
    
    Returns:
        none
    """

    @staticmethod
    def get(course_code, exam_code):
        """This function executes when request method for this route = get
        
        Returns:
            html template -- renders html template
        """

        exam_detail = examdetail_db()
        context = ""

        for item in exam_detail:
            if item['examCode'] == exam_code:
                context = item
        return render_template('exam_detail.html', context=context, quiz=False), 200


class ExamEndpoint(MethodView):
    """View for Exam Route
    
    Arguments:
        MethodView -- If you implement a request method (like GET), it will be used to handle GET requests.
    
    Returns:
        none
    """

    @staticmethod
    def get(course_code, exam_code):
        """This function executes when request method for this route = get
        
        Returns:
            html template -- renders html template
        """
        load_questions = question_db()
        exam_questions = []
        for item in load_questions:
            if item['examCode'] == exam_code:
                exam_questions = item['questions']
        return render_template('exam.html', quiz=True, questions=exam_questions), 200

    @staticmethod
    def post(course_code, exam_code):
        """This function executes when request method for this route = post
        
        Returns:
            str -- The calculated marks for the exam
        """
        examCode = exam_code
        user_inputs = {}
        total_questions = [len(exam['questions']) for exam in question_db() if exam['examCode'] == exam_code]

        question_in_range = list(range(1, total_questions[0] + 1))
        print("Qrange", question_in_range)

        for num in question_in_range:
            name_attr = "Q" + str(num)
            try:
                option = request.form[name_attr]
                print(name_attr, option)
                user_inputs[name_attr] = option
            except KeyError:
                option = None
                user_inputs[name_attr] = option

        print("Inputs", user_inputs)

        ocr_results = ocr(exam_code=examCode,
                          results=user_inputs,
                          num_questions=total_questions[0])

        message_bytes = ocr_results.encode('ascii')
        encoded_msg = base64.b64encode(message_bytes)
        decoded_msg = encoded_msg.decode('ascii')
        return redirect(url_for('show', results=decoded_msg, _external=True))


'''
class ExamMarkingEndpoint(MethodView):

    """View for Exam Marking Route
    
    Arguments:
        MethodView -- If you implement a request method (like POST), it will be used to handle POST requests.
    
    Returns:
        none
    """

    def post(self):
        """This function executes when request method for this route = post
        
        Returns:
            str -- The marks for the exam
        """
        return redirect(url_for('show', results='contact-section'))
'''
