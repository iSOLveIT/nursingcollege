# Third-party modules
from flask.views import MethodView
from flask import render_template, request, redirect, url_for, flash, session

# Local modules
from package.read_json import course_db, question_db, examdetail_db, ExamRemarks
from package.helpers import ocr


class IndexEndpoint(MethodView):
    """View for Index Route
    
    Arguments:
        MethodView -- If you implement a request method (like GET), it will be used to handle GET requests.
    
    Returns:
        get() method
    """

    @staticmethod
    def get():
        """This function executes when request method for this route = get
        
        Returns:
            html template -- renders html template
        """
        return render_template('index.html', quiz=False), 200


class DashboardEndpoint(MethodView):
    """View for Dashboard Route
    
    Arguments:
        MethodView -- If you implement a request method (like GET), it will be used to handle GET requests.
    
    Returns:
        get() method
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
            if str(user_id) in item['registeredStudents']:
                content.append({"courseCode": item['courseCode'],
                                "courseName": item['courseName'],
                                "description": item['description']})
                session['username'] = user_id
        session['course_details'] = content
        return render_template('dashboard.html',
                               course_details=content, quiz=False), 200


class CoursesEndpoint(MethodView):
    """View for Course Route
    
    Arguments:
        MethodView -- If you implement a request method (like GET), it will be used to handle GET requests.
    
    Returns:
        get() method
    """

    @staticmethod
    def get(course_code):
        """This function executes when request method for this route = get
        
        Returns:
            html template -- renders html template
        """
        data = course_db()
        user_id = session.get('username')

        course_detail = {}
        for course in data:
            if course['courseCode'] == course_code and str(user_id) in course['registeredStudents']:
                course_detail = course

        exam_detail = examdetail_db()
        return render_template('course.html',
                               course_code=course_code,
                               course=course_detail,
                               course_exam=exam_detail,
                               quiz=False), 200


class ExamdetailsEndpoint(MethodView):
    """View for Exam Details Route
    
    Arguments:
        MethodView -- If you implement a request method (like GET), it will be used to handle GET requests.
    
    Returns:
        get() method
    """

    @staticmethod
    def get(course_code, exam_code):
        """This function executes when request method for this route = get
        
        Returns:
            html template -- renders html template
        """
        data = course_db()
        user_id = session.get('username')

        content = []
        for item in data:
            if str(user_id) in item['registeredStudents']:
                content.append({"courseCode": item['courseCode'],
                                "courseName": item['courseName'],
                                "description": item['description']})

        exam_detail = examdetail_db()
        context = {}
        for item in exam_detail:
            if item['examCode'] == exam_code:
                context = item

        remarks = ExamRemarks()
        user_remarks = {}
        for remark in remarks.showremarks():
            if remark['courseCode'] == course_code:
                for exam in remark['exams']:
                    if exam['examCode'] == exam_code:
                        for user in exam['participants']:
                            if user['userID'] == session.get('username'):
                                user_remarks = user
                            else:
                                continue

        return render_template('exam_detail.html', context=context, course_details=content,
                               user=user_remarks, quiz=False), 200


class ExamEndpoint(MethodView):
    """View for Exam Route
    
    Arguments:
        MethodView -- If you implement a request method (like GET), it will be used to handle GET requests.
    
    Returns:
        get() and post() methods
    """

    @staticmethod
    def get(course_code, exam_code):
        """This function executes when request method for this route = get
        
        Returns:
            html template -- renders html template
        """
        exam_detail = examdetail_db()
        time_allowed = 0
        for detail in exam_detail:
            if detail['courseCode'] == course_code and detail['examCode'] == exam_code:
                time_allowed += detail['timeAllocated']
        time = time_allowed * 60

        load_questions = question_db()
        exam_questions = []
        for item in load_questions:
            if item['examCode'] == exam_code:
                exam_questions = item['questions']
        return render_template('exam.html', quiz=True,
                               questions=exam_questions, time=time), 200

    @staticmethod
    def post(course_code, exam_code):
        """This function executes when request method for this route = post
        
        Returns:
            str -- The calculated marks for the exam
        """
        exam_code = exam_code
        course_code = course_code
        total_questions = [len(exam['questions']) for exam in question_db() if exam['examCode'] == exam_code]

        question_in_range = list(range(1, total_questions[0] + 1))

        user_inputs = {}
        for num in question_in_range:
            name_attr = "Q" + str(num)
            try:
                option = request.form[name_attr]
                user_inputs[name_attr] = option
            except KeyError:
                option = None
                user_inputs[name_attr] = option

        ocr_results = ocr(exam_code=examCode,
                          results=user_inputs,
                          num_questions=total_questions[0])

        remarks = ExamRemarks()
        remarks.updateremarks(course_code=courseCode,
                              exam_code=examCode,
                              user_id=session.get('username'),
                              content=ocr_results)
        
        return redirect(url_for('examdetails',
                                course_code=course_code,
                                exam_code=exam_code))
