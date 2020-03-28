# Third-party modules
from flask.views import MethodView
from flask import render_template, request, redirect, url_for, flash, session

# Local modules
from package.read_json import  course_db


class IndexEndpoint(MethodView):

    """View for Index Route
    
    Arguments:
        MethodView -- If you implement a request method (like GET), it will be used to handle GET requests.
    
    Returns:
        none
    """
    def get(self):
        """This function executes when request method for this route = get
        
        Returns:
            html template -- renders html template
        """
        return render_template('index.html'), 200
    # This function executes when request method for this route = post

    #def post(self):
        #return redirect(url_for('index', _anchor='contact-section'))


class DashboardEndpoint(MethodView):
    """View for Dashboard Route
    
    Arguments:
        MethodView -- If you implement a request method (like GET), it will be used to handle GET requests.
    
    Returns:
        none
    """
    def get(self, user_id):
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
        return render_template('dashboard.html', username=username, course_details=content), 200


class CoursesEndpoint(MethodView):
    """View for Course Route
    
    Arguments:
        MethodView -- If you implement a request method (like GET), it will be used to handle GET requests.
    
    Returns:
        none
    """
    def get(self, course_code):
        """This function executes when request method for this route = get
        
        Returns:
            html template -- renders html template
        """
        content = session.get('course_details')
        for item in content:
            if item['courseCode'] == course_code:
                course_detail = item
        return render_template('course.html', course_detail=course_detail), 200


class ExamdetailsEndpoint(MethodView):
    """View for Exam Details Route
    
    Arguments:
        MethodView -- If you implement a request method (like GET), it will be used to handle GET requests.
    
    Returns:
        none
    """
    def get(self, course_code, exam_code):
        """This function executes when request method for this route = get
        
        Returns:
            html template -- renders html template
        """
        return render_template('exam_detail.html'), 200


class ExamEndpoint(MethodView):
    """View for Exam Route
    
    Arguments:
        MethodView -- If you implement a request method (like GET), it will be used to handle GET requests.
    
    Returns:
        none
    """
    def get(self, course_code, exam_code):
        """This function executes when request method for this route = get
        
        Returns:
            html template -- renders html template
        """
        return render_template('exam.html'), 200

