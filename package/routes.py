from .views import *
from package import app


# Route for index
app.add_url_rule("/", view_func=IndexEndpoint.as_view("index"))

# Route for dashboard
app.add_url_rule("/dashboard", view_func=DashboardEndpoint.as_view("dashboard"))

# Route for My Courses
app.add_url_rule("/dashboard/courses/<string:_id>", view_func=CoursesEndpoint.as_view("courses"))

# Route for Examdetails
app.add_url_rule("/dashboard/courses/examdetails", view_func=ExamdetailsEndpoint.as_view("examdetails"))

# Route for Exam
app.add_url_rule("//dashboard/courses/examdetails/exam", view_func=ExamEndpoint.as_view("exam"))
