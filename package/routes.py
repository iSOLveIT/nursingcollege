# Local modules
from .views import *
from package import app

# Third-party modules
from flask import request

# Built-in modules
import base64

# Route for Index
app.add_url_rule("/", view_func=IndexEndpoint.as_view("index"))

# Route for Dashboard
app.add_url_rule("/dashboard/<string:user_id>", view_func=DashboardEndpoint.as_view("dashboard"))

# Route for My Courses
app.add_url_rule("/courses/<string:course_code>", view_func=CoursesEndpoint.as_view("courses"))

# Route for Exam Details
app.add_url_rule("/courses/<string:course_code>/examdetails/<string:exam_code>", view_func=ExamdetailsEndpoint.as_view("examdetails"))

# Route for Exam
app.add_url_rule("/courses/<string:course_code>/examdetails/<string:exam_code>/exam", view_func=ExamEndpoint.as_view("exam"))

# Route for Exam Marking
# app.add_url_rule("/courses/<string:course_code>/examdetails/<string:exam_code>/exam/results", view_func=ExamMarkingEndpoint.as_view("results"))


# Test
@app.route("/show")
def show():
    results = str(request.args['results'])
    message_bytes = results.encode('ascii')
    encoded_msg = base64.b64decode(message_bytes)
    decoded_msg = encoded_msg.decode('ascii')
    return f"<h1> {decoded_msg} </h1>"