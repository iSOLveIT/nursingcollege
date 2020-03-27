# Third-party modules
from flask.views import MethodView
from flask import render_template, request, redirect, url_for, flash


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
        return render_template('dashboard.html'), 200


class CoursesEndpoint(MethodView):
    """View for Index Route
    
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
        return render_template('course.html'), 200


class ExamdetailsEndpoint(MethodView):
    """View for Index Route
    
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
    """View for Index Route
    
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

