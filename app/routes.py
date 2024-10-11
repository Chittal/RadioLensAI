from flask import Blueprint, render_template

# Create a blueprint for the app routes
main_routes = Blueprint('main', __name__)

# Define the route for the home page
@main_routes.route('/')
def home():
    return render_template('home.html')

# Define the route for the profile page
@main_routes.route('/profile')
def profile():
    return render_template('profile.html')

# Define the route for the generate report page
@main_routes.route('/generate_report')
def generate_report():
    return render_template('generate_report.html')

# Define the route for the reports page
@main_routes.route('/view_reports')
def view_reports():
    return render_template('view_reports.html')

# Define the route for the contact us page
@main_routes.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')
